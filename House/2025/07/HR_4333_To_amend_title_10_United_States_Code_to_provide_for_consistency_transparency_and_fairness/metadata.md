# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4333?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4333
- Title: Qualified to Serve Act
- Congress: 119
- Bill type: HR
- Bill number: 4333
- Origin chamber: House
- Introduced date: 2025-07-10
- Update date: 2025-12-10T09:05:49Z
- Update date including text: 2025-12-10T09:05:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-10: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-07-10: Introduced in House

## Actions

- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-10",
    "latestAction": {
      "actionDate": "2025-07-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4333",
    "number": "4333",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "K000399",
        "district": "2",
        "firstName": "Jennifer",
        "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
        "lastName": "Kiggans",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "Qualified to Serve Act",
    "type": "HR",
    "updateDate": "2025-12-10T09:05:49Z",
    "updateDateIncludingText": "2025-12-10T09:05:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-10",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-10",
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
          "date": "2025-07-10T15:08:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "W000804",
      "district": "1",
      "firstName": "Robert",
      "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Wittman",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "VA"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "NC"
    },
    {
      "bioguideId": "G000593",
      "district": "28",
      "firstName": "Carlos",
      "fullName": "Rep. Gimenez, Carlos A. [R-FL-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Gimenez",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "FL"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "NE"
    },
    {
      "bioguideId": "M001210",
      "district": "3",
      "firstName": "Gregory",
      "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "NC"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham J. [R-AZ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-07-14",
      "state": "AZ"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "MA"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-08-15",
      "state": "KS"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "PA"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4333ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4333\nIN THE HOUSE OF REPRESENTATIVES\nJuly 10, 2025 Mrs. Kiggans of Virginia (for herself, Mr. Wittman , Mr. Davis of North Carolina , Mr. Gimenez , Mr. Bacon , and Mr. Murphy ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo amend title 10, United States Code, to provide for consistency, transparency, and fairness with respect to medical evaluations to determine fitness to serve as members of the Armed Forces, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Qualified to Serve Act .\n#### 2. Medical accession standards for members of the Armed Forces\nChapter 37 of title 10, United States Code, is amended by adding at the end the following new section:\n658. Medical accession standards for members of the Armed Forces (a) Establishment of Standards (1) The Secretaries concerned shall establish uniform medical accession standards for each Armed Force. Such standards shall\u2014 (A) apply uniformly for all commissioned officers of an Armed Force; and (B) apply uniformly for all enlisted members of an Armed Force across each occupational specialty. (2) The Secretary concerned shall make readily available and understandable to potential members of the Armed Forces the standards established under paragraph (1), including an explanation of the process established under subsection (c)(1) and the process for seeking approval under subsection (c)(2). (b) Prohibition on Certain Medical Disqualifications No person may be disqualified from serving as a member of the Armed Forces on the sole basis of a past diagnosis of a medical condition if\u2014 (1) the diagnosis occurred before such person reached the age of 13 years old; (2) the condition did not require treatment during the five-year period that ends on the date on which such person seeks to become a member of the Armed Forces; (3) a licensed medical professional provides a current evaluation affirming that such person does not meet diagnostic criteria for the condition and is medically fit for service as a member of the Armed Forces; and (4) the Secretary concerned determines such diagnosis is unlikely to impact the health and readiness of the Armed Force of which such person seeks to become a member. (c) Process for Review or Waiver of Medical Disqualifications (1) The Secretary concerned shall establish a process for the review of medical disqualifications of persons seeking to become a member of the Armed Forces. (2) The Secretary concerned may approve the accession of a person into the Armed Forces without regard to a disqualifying medical diagnosis if the Secretary concerned determines that the accession of such person is in the interests of national security. (d) Annual Report The Secretary of Defense shall annually submit to the congressional defense committees a report identifying\u2014 (1) the number of persons disqualified from service as a member of the Armed Forces during the preceding calendar year due to medical history; (2) the number and type of approvals granted under subsection (c)(2) during the preceding calendar year; and (3) any updates to the medical standards for accession established under subsection (a) or the process established under subsection (c)(1) since the submission of the preceding report. .",
      "versionDate": "2025-07-10",
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
        "updateDate": "2025-08-07T18:39:09Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4333ih.xml"
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
      "title": "Qualified to Serve Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T03:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Qualified to Serve Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-23T03:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 10, United States Code, to provide for consistency, transparency, and fairness with respect to medical evaluations to determine fitness to serve as members of the Armed Forces, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-23T03:33:33Z"
    }
  ]
}
```
