# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5629?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5629
- Title: To provide that the final rule of the Department of Health and Human Services titled "Medications for the Treatment of Opioid Use Disorder", except for the portion of the final rule relating to accreditation of opioid treatment programs, shall have no force or effect.
- Congress: 119
- Bill type: HR
- Bill number: 5629
- Origin chamber: House
- Introduced date: 2025-09-30
- Update date: 2026-01-12T21:40:41Z
- Update date including text: 2026-01-12T21:40:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-09-30: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-09-30: Introduced in House

## Actions

- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-30",
    "latestAction": {
      "actionDate": "2025-09-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5629",
    "number": "5629",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "H001093",
        "district": "9",
        "firstName": "Erin",
        "fullName": "Rep. Houchin, Erin [R-IN-9]",
        "lastName": "Houchin",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "To provide that the final rule of the Department of Health and Human Services titled \"Medications for the Treatment of Opioid Use Disorder\", except for the portion of the final rule relating to accreditation of opioid treatment programs, shall have no force or effect.",
    "type": "HR",
    "updateDate": "2026-01-12T21:40:41Z",
    "updateDateIncludingText": "2026-01-12T21:40:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-30",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2025-09-30T16:03:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5629ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5629\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 30, 2025 Mrs. Houchin introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo provide that the final rule of the Department of Health and Human Services titled Medications for the Treatment of Opioid Use Disorder , except for the portion of the final rule relating to accreditation of opioid treatment programs, shall have no force or effect.\n#### 1. Rule relating to medications for the treatment of opioid use disorder\n##### (a) In general\nExcept as provided by subsection (b), the final rule of the Department of Health and Human Services titled Medications for the Treatment of Opioid Use Disorder (89 Fed. Reg. 7549; published February 2, 2024) shall have no force or effect.\n##### (b) Exception\nSubsection (a) shall not apply to the portion of the final rule that makes modifications to subpart B of part 8 of title 42, Code of Federal Regulations (relating to accreditation of opioid treatment programs).",
      "versionDate": "2025-09-30",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-12-17T16:48:41Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-30",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr5629",
          "measure-number": "5629",
          "measure-type": "hr",
          "orig-publish-date": "2025-09-30",
          "originChamber": "HOUSE",
          "update-date": "2026-01-12"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5629v00",
            "update-date": "2026-01-12"
          },
          "action-date": "2025-09-30",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill nullifies part of\u00a0the final rule issued by the Department of Health and Human Services (HHS) titled <em>Medications for the Treatment of Opioid Use Disorder</em> and published on February 2, 2024.</p><p>The rule incorporated into regulations certain flexibilities for opioid treatment that were initially implemented during the COVID-19 public health emergency. The bill nullifies these flexibilities, including (1)\u00a0expanded flexibility for patients in their first or second month of treatment to receive take-home doses of methadone,\u00a0(2)\u00a0flexibility to use telehealth examinations to admit patients for treatment involving buprenorphine or methadone, and (3)\u00a0expanded access to evidence-based practices such as splitting doses for certain patients.\u00a0</p><p>Pursuant to a statutory requirement, the rule also allowed patients to be admitted to an opioid treatment program without having to show at least a one-year history of opioid misuse. The bill nullifies these provisions of the rule.</p>"
        },
        "title": "To provide that the final rule of the Department of Health and Human Services titled \"Medications for the Treatment of Opioid Use Disorder\", except for the portion of the final rule relating to accreditation of opioid treatment programs, shall have no force or effect."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5629.xml",
    "summary": {
      "actionDate": "2025-09-30",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill nullifies part of\u00a0the final rule issued by the Department of Health and Human Services (HHS) titled <em>Medications for the Treatment of Opioid Use Disorder</em> and published on February 2, 2024.</p><p>The rule incorporated into regulations certain flexibilities for opioid treatment that were initially implemented during the COVID-19 public health emergency. The bill nullifies these flexibilities, including (1)\u00a0expanded flexibility for patients in their first or second month of treatment to receive take-home doses of methadone,\u00a0(2)\u00a0flexibility to use telehealth examinations to admit patients for treatment involving buprenorphine or methadone, and (3)\u00a0expanded access to evidence-based practices such as splitting doses for certain patients.\u00a0</p><p>Pursuant to a statutory requirement, the rule also allowed patients to be admitted to an opioid treatment program without having to show at least a one-year history of opioid misuse. The bill nullifies these provisions of the rule.</p>",
      "updateDate": "2026-01-12",
      "versionCode": "id119hr5629"
    },
    "title": "To provide that the final rule of the Department of Health and Human Services titled \"Medications for the Treatment of Opioid Use Disorder\", except for the portion of the final rule relating to accreditation of opioid treatment programs, shall have no force or effect."
  },
  "summaries": [
    {
      "actionDate": "2025-09-30",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill nullifies part of\u00a0the final rule issued by the Department of Health and Human Services (HHS) titled <em>Medications for the Treatment of Opioid Use Disorder</em> and published on February 2, 2024.</p><p>The rule incorporated into regulations certain flexibilities for opioid treatment that were initially implemented during the COVID-19 public health emergency. The bill nullifies these flexibilities, including (1)\u00a0expanded flexibility for patients in their first or second month of treatment to receive take-home doses of methadone,\u00a0(2)\u00a0flexibility to use telehealth examinations to admit patients for treatment involving buprenorphine or methadone, and (3)\u00a0expanded access to evidence-based practices such as splitting doses for certain patients.\u00a0</p><p>Pursuant to a statutory requirement, the rule also allowed patients to be admitted to an opioid treatment program without having to show at least a one-year history of opioid misuse. The bill nullifies these provisions of the rule.</p>",
      "updateDate": "2026-01-12",
      "versionCode": "id119hr5629"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5629ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide that the final rule of the Department of Health and Human Services titled \"Medications for the Treatment of Opioid Use Disorder\", except for the portion of the final rule relating to accreditation of opioid treatment programs, shall have no force or effect.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-04T10:18:12Z"
    },
    {
      "title": "To provide that the final rule of the Department of Health and Human Services titled \"Medications for the Treatment of Opioid Use Disorder\", except for the portion of the final rule relating to accreditation of opioid treatment programs, shall have no force or effect.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-01T08:06:22Z"
    }
  ]
}
```
