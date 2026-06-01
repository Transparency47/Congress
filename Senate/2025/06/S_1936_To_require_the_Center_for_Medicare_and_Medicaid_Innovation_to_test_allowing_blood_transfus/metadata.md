# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1936?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1936
- Title: Improving Access to Transfusion Care for Hospice Patients Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1936
- Origin chamber: Senate
- Introduced date: 2025-06-03
- Update date: 2025-07-25T15:42:54Z
- Update date including text: 2025-07-25T15:42:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-06-03: Introduced in Senate
- 2025-06-03 - IntroReferral: Introduced in Senate
- 2025-06-03 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-06-03: Introduced in Senate

## Actions

- 2025-06-03 - IntroReferral: Introduced in Senate
- 2025-06-03 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-03",
    "latestAction": {
      "actionDate": "2025-06-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1936",
    "number": "1936",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "R000608",
        "district": "",
        "firstName": "Jacky",
        "fullName": "Sen. Rosen, Jacky [D-NV]",
        "lastName": "Rosen",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Improving Access to Transfusion Care for Hospice Patients Act of 2025",
    "type": "S",
    "updateDate": "2025-07-25T15:42:54Z",
    "updateDateIncludingText": "2025-07-25T15:42:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-03",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-06-03T19:30:53Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "WY"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1936is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1936\nIN THE SENATE OF THE UNITED STATES\nJune 3, 2025 Ms. Rosen (for herself, Mr. Barrasso , and Ms. Baldwin ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo require the Center for Medicare and Medicaid Innovation to test allowing blood transfusions to be paid separately from the Medicare hospice all-inclusive per diem payment.\n#### 1. Short title\nThis Act may be cited as the Improving Access to Transfusion Care for Hospice Patients Act of 2025 .\n#### 2. Center for Medicare and Medicaid Innovation testing of allowing blood transfusions to be paid separately from the Medicare hospice all-inclusive per diem payment\nSection 1115A of the Social Security Act ( 42 U.S.C. 1315a ) is amended\u2014\n**(1)**\nin subsection (b)(2)(A), by adding at the end the following new sentence: \u201cThe models selected under this subparagraph shall include the testing of the model described in subsection (h).\u201d; and\n**(2)**\nby adding at the end the following new subsection:\n(h) Testing of allowing blood transfusions To be paid separately from the Medicare hospice all-Inclusive per diem payment (1) In general Not later than 1 year after the date of enactment of this subsection, the CMI shall establish and implement a model under which blood transfusions furnished to an individual receiving hospice care are paid separately from the hospice all-inclusive per diem payment under section 1814(i). The separate payment amount for such blood transfusion shall be the amount that would otherwise apply under title XVIII if the transfusion was not furnished as part of hospice care. (2) Requirements for evaluation In conducting any evaluation of the model described in paragraph (1) pursuant to subsection (b)(4), the CMI shall ensure it compares participants under the model with similar patients outside of the model with respect to the following metrics: (A) The number of chemotherapy services furnished in the last 14 days of life. (B) Hospital utilization in the last 30 days of life, including emergency department visits, in-patient and observation status stays (including the length of the stays), and intensive care unit (ICU) days. (C) How many days receiving hospice care before the end of life. (D) The number of patients receiving hospice care who received a transfusion compared to patients with similar diagnoses not receiving hospice care. (E) The average frequency of transfusion for patients receiving hospice care compared to patients not receiving hospice care. (F) The number of transfusions for patients receiving hospice care compared to patients not receiving hospice care. (G) Other areas determined appropriate by the CMI. .",
      "versionDate": "2025-06-03",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2025-06-23T14:18:41Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-03",
    "originChamber": "Senate",
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
          "measure-id": "id119s1936",
          "measure-number": "1936",
          "measure-type": "s",
          "orig-publish-date": "2025-06-03",
          "originChamber": "SENATE",
          "update-date": "2025-07-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1936v00",
            "update-date": "2025-07-25"
          },
          "action-date": "2025-06-03",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Improving Access to Transfusion Care for Hospice Patients Act of </strong><strong>2025</strong></p><p>This bill requires the Center for Medicare and Medicaid Innovation (CMMI) to test a model under which blood transfusions furnished to an individual receiving hospice care are paid separately from the hospice all-inclusive per diem payment under Medicare. The CMMI must evaluate the model by comparing patients participating in the model with those outside of the model in relation to specified metrics, such as hospital utilization and days of hospice care before the end of life.</p>"
        },
        "title": "Improving Access to Transfusion Care for Hospice Patients Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1936.xml",
    "summary": {
      "actionDate": "2025-06-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Improving Access to Transfusion Care for Hospice Patients Act of </strong><strong>2025</strong></p><p>This bill requires the Center for Medicare and Medicaid Innovation (CMMI) to test a model under which blood transfusions furnished to an individual receiving hospice care are paid separately from the hospice all-inclusive per diem payment under Medicare. The CMMI must evaluate the model by comparing patients participating in the model with those outside of the model in relation to specified metrics, such as hospital utilization and days of hospice care before the end of life.</p>",
      "updateDate": "2025-07-25",
      "versionCode": "id119s1936"
    },
    "title": "Improving Access to Transfusion Care for Hospice Patients Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-06-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Improving Access to Transfusion Care for Hospice Patients Act of </strong><strong>2025</strong></p><p>This bill requires the Center for Medicare and Medicaid Innovation (CMMI) to test a model under which blood transfusions furnished to an individual receiving hospice care are paid separately from the hospice all-inclusive per diem payment under Medicare. The CMMI must evaluate the model by comparing patients participating in the model with those outside of the model in relation to specified metrics, such as hospital utilization and days of hospice care before the end of life.</p>",
      "updateDate": "2025-07-25",
      "versionCode": "id119s1936"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1936is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Improving Access to Transfusion Care for Hospice Patients Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-10T02:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Improving Access to Transfusion Care for Hospice Patients Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-10T02:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Center for Medicare and Medicaid Innovation to test allowing blood transfusions to be paid separately from the Medicare hospice all-inclusive per diem payment.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-10T02:48:23Z"
    }
  ]
}
```
