# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2244?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2244
- Title: Michael Lecik Military Firefighters Protection Act
- Congress: 119
- Bill type: HR
- Bill number: 2244
- Origin chamber: House
- Introduced date: 2025-03-21
- Update date: 2025-12-19T09:07:41Z
- Update date including text: 2025-12-19T09:07:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-21: Introduced in House
- 2025-03-21 - IntroReferral: Introduced in House
- 2025-03-21 - IntroReferral: Introduced in House
- 2025-03-21 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-04-04 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.
- Latest action: 2025-03-21: Introduced in House

## Actions

- 2025-03-21 - IntroReferral: Introduced in House
- 2025-03-21 - IntroReferral: Introduced in House
- 2025-03-21 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-04-04 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-21",
    "latestAction": {
      "actionDate": "2025-03-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2244",
    "number": "2244",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001298",
        "district": "2",
        "firstName": "Don",
        "fullName": "Rep. Bacon, Don [R-NE-2]",
        "lastName": "Bacon",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Michael Lecik Military Firefighters Protection Act",
    "type": "HR",
    "updateDate": "2025-12-19T09:07:41Z",
    "updateDateIncludingText": "2025-12-19T09:07:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-04",
      "committees": {
        "item": {
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Disability Assistance and Memorial Affairs.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-21",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-21",
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
          "date": "2025-03-21T20:00:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-04T18:10:11Z",
              "name": "Referred to"
            }
          },
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "C001121",
      "district": "6",
      "firstName": "Jason",
      "fullName": "Rep. Crow, Jason [D-CO-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Crow",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "CO"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "VA"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "NY"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "CO"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2244ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2244\nIN THE HOUSE OF REPRESENTATIVES\nMarch 21, 2025 Mr. Bacon introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to establish presumptions of service connection for diseases associated with firefighting.\n#### 1. Short title\nThis Act may be cited as the Michael Lecik Military Firefighters Protection Act .\n#### 2. Presumptions of service connection for diseases associated with firefighting\n##### (a) Establishment\nSubchapter II of chapter 11 of title 38, United States Code, is amended by adding at the end the following new section:\n1120A. Presumptions of service connection for diseases associated with firefighting (a) Service connection For the purposes of section 1110 of this title, and subject to section 1113 of this title, a disease specified in subsection (b) becoming manifest in a veteran described in subsection (c) to a degree of disability specified in subsection (d) and within the period specified in subsection (e) shall be considered to have been incurred in or aggravated during active military, naval, or air service, notwithstanding that there is no record of evidence of such disease during a period of such service. (b) Specified diseases The diseases specified in this subsection are the following: (1) Heart disease. (2) Lung disease. (3) Brain cancer. (4) Cancer of the blood or lymphatic systems. (5) Leukemia. (6) Lymphoma (except Hodgkin\u2019s disease). (7) Multiple myeloma. (8) Bladder cancer. (9) Kidney cancer. (10) Cancer of the reproductive system (including testicular cancer). (11) Cancer of the digestive system. (12) Colon cancer. (13) Liver cancer. (14) Skin cancer. (15) Lung cancer. (16) Breast cancer. (17) Each additional disease (if any) that the Secretary determines in regulations prescribed under this section\u2014 (A) warrants a presumption of service connection by reason of having positive association with firefighting; and (B) becomes manifest within the period (if any) prescribed in such regulations in a veteran described in subsection (c), not\u00adwith\u00adstand\u00ading subsection (e). (c) Covered veterans A veteran described in this subsection is a veteran who\u2014 (1) is trained in fire suppression; and (2) served on active duty in a military occupational specialty or career field with a primary responsibility for firefighting or damage control for at least five years in the aggregate. (d) Degree of disability The degree of disability specified in this subsection is 10 percent or more. (e) Period The period specified in this subsection is within 15 years of the date on which the veteran separated from active military, naval, or air service. (f) Effective date of award The effective date of an award under this section shall be determined in accordance with section 5110 of this title. .\n##### (b) Clerical amendment\nThe table of sections at the beginning of such chapter is amended by inserting after the item relating to section 1120 the following new item:\n1120A. Presumptions of service connection for diseases associated with firefighting. .",
      "versionDate": "2025-03-21",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-08T13:54:55Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-21",
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
          "measure-id": "id119hr2244",
          "measure-number": "2244",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-21",
          "originChamber": "HOUSE",
          "update-date": "2025-06-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2244v00",
            "update-date": "2025-06-25"
          },
          "action-date": "2025-03-21",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Michael Lecik Military Firefighters Protection Act</strong></p><p>This bill establishes a presumption of service-connection for specified diseases becoming manifest in certain military firefighter veterans to a degree of disability of 10% or more within 15 years of the veteran's separation from active military, naval, or air service. Under a presumption of service-connection, specific diseases or disabilities diagnosed in certain veterans are presumed to have been caused by the circumstances of their military service. Health care benefits and disability compensation may then be awarded.</p><p>Veterans addressed by this bill are those who (1) are trained in fire suppression, and (2) served on active duty in a military occupational specialty or career field with a primary responsibility of firefighting or damage control for at least five years in the aggregate.</p>"
        },
        "title": "Michael Lecik Military Firefighters Protection Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2244.xml",
    "summary": {
      "actionDate": "2025-03-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Michael Lecik Military Firefighters Protection Act</strong></p><p>This bill establishes a presumption of service-connection for specified diseases becoming manifest in certain military firefighter veterans to a degree of disability of 10% or more within 15 years of the veteran's separation from active military, naval, or air service. Under a presumption of service-connection, specific diseases or disabilities diagnosed in certain veterans are presumed to have been caused by the circumstances of their military service. Health care benefits and disability compensation may then be awarded.</p><p>Veterans addressed by this bill are those who (1) are trained in fire suppression, and (2) served on active duty in a military occupational specialty or career field with a primary responsibility of firefighting or damage control for at least five years in the aggregate.</p>",
      "updateDate": "2025-06-25",
      "versionCode": "id119hr2244"
    },
    "title": "Michael Lecik Military Firefighters Protection Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Michael Lecik Military Firefighters Protection Act</strong></p><p>This bill establishes a presumption of service-connection for specified diseases becoming manifest in certain military firefighter veterans to a degree of disability of 10% or more within 15 years of the veteran's separation from active military, naval, or air service. Under a presumption of service-connection, specific diseases or disabilities diagnosed in certain veterans are presumed to have been caused by the circumstances of their military service. Health care benefits and disability compensation may then be awarded.</p><p>Veterans addressed by this bill are those who (1) are trained in fire suppression, and (2) served on active duty in a military occupational specialty or career field with a primary responsibility of firefighting or damage control for at least five years in the aggregate.</p>",
      "updateDate": "2025-06-25",
      "versionCode": "id119hr2244"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2244ih.xml"
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
      "title": "Michael Lecik Military Firefighters Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-27T01:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Michael Lecik Military Firefighters Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T01:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to establish presumptions of service connection for diseases associated with firefighting.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T01:48:26Z"
    }
  ]
}
```
