# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2356?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2356
- Title: ADAPT Act
- Congress: 119
- Bill type: S
- Bill number: 2356
- Origin chamber: Senate
- Introduced date: 2025-07-17
- Update date: 2026-02-13T12:03:21Z
- Update date including text: 2026-02-13T12:03:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-07-17: Introduced in Senate
- 2025-07-17 - IntroReferral: Introduced in Senate
- 2025-07-17 - IntroReferral: Read twice and referred to the Committee on Finance. (text: CR S4459)
- Latest action: 2025-07-17: Introduced in Senate

## Actions

- 2025-07-17 - IntroReferral: Introduced in Senate
- 2025-07-17 - IntroReferral: Read twice and referred to the Committee on Finance. (text: CR S4459)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-17",
    "latestAction": {
      "actionDate": "2025-07-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2356",
    "number": "2356",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001261",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Barrasso, John [R-WY]",
        "lastName": "Barrasso",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "ADAPT Act",
    "type": "S",
    "updateDate": "2026-02-13T12:03:21Z",
    "updateDateIncludingText": "2026-02-13T12:03:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-17",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance. (text: CR S4459)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-17",
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
        "item": [
          {
            "date": "2025-07-17T21:57:11Z",
            "name": "Referred To"
          },
          {
            "date": "2025-07-17T21:57:11Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "CO"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2356is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2356\nIN THE SENATE OF THE UNITED STATES\nJuly 17, 2025 Mr. Barrasso (for himself and Mr. Bennet ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo expand psychological mental and behavioral health services to Medicare, Medicaid, and CHIP beneficiaries by permitting reimbursement of psychological services provided by certain supervised psychology trainees, and facilitating the reimbursement of those services.\n#### 1. Short title\nThis Act may be cited as the Accelerating the Development of Advanced Psychology Trainees Act or the ADAPT Act .\n#### 2. Coverage and coding for qualified psychologist services furnished by advanced psychology trainees under the Medicare program\n##### (a) Coverage\n**(1) In general**\nSection 1861(ii) of the Social Security Act ( 42 U.S.C. 1395x(ii) ) is amended\u2014\n**(A)**\nby inserting (1) after (ii) ;\n**(B)**\nin paragraph (1), as added by subparagraph (A), by inserting (or furnished by an advanced psychology trainee under the general supervision of a clinical psychologist (as so defined) and billed by the supervising psychologist) after (as defined by the Secretary) ; and\n**(C)**\nby adding at the end the following new paragraph:\n(2) In this subsection: (A) The term advanced psychology trainee means\u2014 (i) a doctoral intern who is completing a required period of supervised experiential training through a program accredited by the American Psychological Association, not less than one year in duration, before being awarded a doctoral degree; or (ii) a postdoctoral resident who has obtained a doctoral degree in psychology, is seeking a license to practice psychology, and is engaged in a 1- or 2-year period of additional supervised experiential training to acquire the skills or hours required for licensure through a program accredited by the American Psychological Association or a member of the Association of Psychology Postdoctoral and Internship Centers. (B) The term general supervision means, with respect to a service, that the service is furnished under the overall direction and control of a clinical psychologist (as defined for purposes of paragraph (1)), but the supervising psychologist's presence is not required during the furnishing of the service. .\n**(2) Effective date**\nThe amendments made by this subsection shall apply to services furnished on or after the date that is 1 year after the date of the enactment of this Act.\n##### (b) Development of GC modifier code\nNot later than 1 year after the date of the enactment of this Act, the Secretary of Health and Human Services shall develop a GC modifier code to identify and accurately bill for services furnished by an advanced psychology trainee pursuant to the amendments made by subsection (a).\n#### 3. Guidance to States on coverage of services provided by advanced psychology trainees under Medicaid and CHIP\nNot later than 1 year after the date of enactment of this Act, the Secretary of Health and Human Services shall issue and disseminate guidance to States on strategies to overcome existing barriers to coverage of services furnished by advanced psychology trainees (as defined under section 1861(ii)(2) of the Social Security Act, as added by section 2(a), through the Medicaid program under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ) and the Children\u2019s Health Insurance Program under title XXI of such Act ( 42 U.S.C. 1397aa et seq. )). Such guidance shall include technical assistance and best practices regarding each of the following:\n**(1)**\nRecommended legal mechanisms for activating coverage of services furnished by advanced psychology trainees under such programs.\n**(2)**\nRecommended billing codes and code modifiers for services furnished by advanced psychology trainees.\n**(3)**\nExamples of States that have used waivers under the Medicaid program or Children's Health Insurance Program to enable coverage of services furnished by advanced psychology trainees under such programs.",
      "versionDate": "2025-07-17",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-07-17",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4484",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "ADAPT Act",
      "type": "HR"
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
        "updateDate": "2025-09-12T15:22:19Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-17",
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
          "measure-id": "id119s2356",
          "measure-number": "2356",
          "measure-type": "s",
          "orig-publish-date": "2025-07-17",
          "originChamber": "SENATE",
          "update-date": "2025-12-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2356v00",
            "update-date": "2025-12-02"
          },
          "action-date": "2025-07-17",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Accelerating the Development of Advanced Psychology Trainees Act or the ADAPT Act</strong></p><p>This bill provides for Medicare coverage of services that are furnished by advanced psychology trainees. It also requires the Centers for Medicare & Medicaid Services to issue guidance for states on coverage options for such services under Medicaid and the Children's Health Insurance Program (CHIP).<br/></p>"
        },
        "title": "ADAPT Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2356.xml",
    "summary": {
      "actionDate": "2025-07-17",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Accelerating the Development of Advanced Psychology Trainees Act or the ADAPT Act</strong></p><p>This bill provides for Medicare coverage of services that are furnished by advanced psychology trainees. It also requires the Centers for Medicare & Medicaid Services to issue guidance for states on coverage options for such services under Medicaid and the Children's Health Insurance Program (CHIP).<br/></p>",
      "updateDate": "2025-12-02",
      "versionCode": "id119s2356"
    },
    "title": "ADAPT Act"
  },
  "summaries": [
    {
      "actionDate": "2025-07-17",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Accelerating the Development of Advanced Psychology Trainees Act or the ADAPT Act</strong></p><p>This bill provides for Medicare coverage of services that are furnished by advanced psychology trainees. It also requires the Centers for Medicare & Medicaid Services to issue guidance for states on coverage options for such services under Medicaid and the Children's Health Insurance Program (CHIP).<br/></p>",
      "updateDate": "2025-12-02",
      "versionCode": "id119s2356"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2356is.xml"
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
      "title": "ADAPT Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-13T12:03:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "ADAPT Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-02T03:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Accelerating the Development of Advanced Psychology Trainees Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-02T03:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to expand psychological mental and behavioral health services to Medicare, Medicaid, and CHIP beneficiaries by permitting reimbursement of psychological services provided by certain supervised psychology trainees, and facilitating the reimbursement of those services.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-02T03:18:22Z"
    }
  ]
}
```
