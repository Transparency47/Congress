# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1143?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1143
- Title: Recognizing the 205th anniversary of the War of Greek Independence.
- Congress: 119
- Bill type: HRES
- Bill number: 1143
- Origin chamber: House
- Introduced date: 2026-03-27
- Update date: 2026-05-06T14:41:46Z
- Update date including text: 2026-05-06T14:41:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-03-27: Introduced in House
- 2026-03-27 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-03-27 - IntroReferral: Submitted in House
- 2026-03-27 - IntroReferral: Submitted in House
- Latest action: 2026-03-27: Submitted in House

## Actions

- 2026-03-27 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-03-27 - IntroReferral: Submitted in House
- 2026-03-27 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-27",
    "latestAction": {
      "actionDate": "2026-03-27",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1143",
    "number": "1143",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "B001257",
        "district": "12",
        "firstName": "Gus",
        "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
        "lastName": "Bilirakis",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Recognizing the 205th anniversary of the War of Greek Independence.",
    "type": "HRES",
    "updateDate": "2026-05-06T14:41:46Z",
    "updateDateIncludingText": "2026-05-06T14:41:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-27",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-03-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2026-03-28T01:32:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2026-03-27",
      "state": "NH"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2026-03-27",
      "state": "NY"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2026-03-27",
      "state": "NV"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2026-03-27",
      "state": "FL"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2026-03-27",
      "state": "NH"
    },
    {
      "bioguideId": "P000034",
      "district": "6",
      "firstName": "Frank",
      "fullName": "Rep. Pallone, Frank [D-NJ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Pallone",
      "party": "D",
      "sponsorshipDate": "2026-03-27",
      "state": "NJ"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2026-03-27",
      "state": "CA"
    },
    {
      "bioguideId": "M001226",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Menendez, Robert [D-NJ-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Menendez",
      "party": "D",
      "sponsorshipDate": "2026-03-27",
      "state": "NJ"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2026-03-27",
      "state": "RI"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2026-03-27",
      "state": "NY"
    },
    {
      "bioguideId": "A000380",
      "district": "1",
      "firstName": "Gabe",
      "fullName": "Rep. Amo, Gabe [D-RI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Amo",
      "party": "D",
      "sponsorshipDate": "2026-03-27",
      "state": "RI"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-04-02",
      "state": "NY"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-04-02",
      "state": "NJ"
    },
    {
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2026-04-02",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1143ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1143\nIN THE HOUSE OF REPRESENTATIVES\nMarch 27, 2026 Mr. Bilirakis (for himself, Mr. Pappas , Ms. Malliotakis , Ms. Titus , Mr. Haridopolos , Ms. Goodlander , Mr. Pallone , Mr. Costa , Mr. Menendez , Mr. Magaziner , Ms. Meng , and Mr. Amo ) submitted the following resolution; which was referred to the Committee on Foreign Affairs\nRESOLUTION\nRecognizing the 205th anniversary of the War of Greek Independence.\nThat the House of Representatives\u2014\n**(1)**\nextends warm congratulations and best wishes to the people of Greece as they celebrate the 205th anniversary of the War of Greek Independence;\n**(2)**\nexpresses support for the principles of democracy, human rights, and the rule of law to which the people of the United States and Greece are committed;\n**(3)**\nnotes the important role that Greece has played in the wider European region and in the community of nations since gaining its independence;\n**(4)**\ncommends the Greek-American community for its contributions to the United States and its role as a bridge between the two countries;\n**(5)**\ncommends the geostrategic importance of Greece at the junction of three continents, and in particular, the critical role Greece plays in promoting stability in the Eastern Mediterranean and Western Balkans and in continuously upholding international law and respect for national sovereignty and territorial integrity; and\n**(6)**\nappreciates the deepening cooperation between the United States and Greece, based on shared values and interests, including the important bilateral energy and security partnership and the important role that Greece plays in bolstering European energy security.",
      "versionDate": "2026-03-27",
      "versionType": "IH"
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
        "actionDate": "2025-03-25",
        "text": "Referred to the House Committee on Foreign Affairs."
      },
      "number": "249",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Recognizing the 204th anniversary of the War of Greek Independence.",
      "type": "HRES"
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
        "name": "International Affairs",
        "updateDate": "2026-03-30T22:46:53Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-03-27",
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
          "measure-id": "id119hres1143",
          "measure-number": "1143",
          "measure-type": "hres",
          "orig-publish-date": "2026-03-27",
          "originChamber": "HOUSE",
          "update-date": "2026-05-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres1143v00",
            "update-date": "2026-05-06"
          },
          "action-date": "2026-03-27",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution congratulates the people of Greece as they celebrate the 205th anniversary of the War of Greek Independence. The resolution also expresses support for the principles of democracy, human rights, and the rule of law to which the people of the United States and Greece are committed.</p>"
        },
        "title": "Recognizing the 205th anniversary of the War of Greek Independence."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres1143.xml",
    "summary": {
      "actionDate": "2026-03-27",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution congratulates the people of Greece as they celebrate the 205th anniversary of the War of Greek Independence. The resolution also expresses support for the principles of democracy, human rights, and the rule of law to which the people of the United States and Greece are committed.</p>",
      "updateDate": "2026-05-06",
      "versionCode": "id119hres1143"
    },
    "title": "Recognizing the 205th anniversary of the War of Greek Independence."
  },
  "summaries": [
    {
      "actionDate": "2026-03-27",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution congratulates the people of Greece as they celebrate the 205th anniversary of the War of Greek Independence. The resolution also expresses support for the principles of democracy, human rights, and the rule of law to which the people of the United States and Greece are committed.</p>",
      "updateDate": "2026-05-06",
      "versionCode": "id119hres1143"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1143ih.xml"
        }
      ],
      "type": "IH"
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
      "title": "Recognizing the 205th anniversary of the War of Greek Independence.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-28T12:18:25Z"
    },
    {
      "title": "Recognizing the 205th anniversary of the War of Greek Independence.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-28T08:06:35Z"
    }
  ]
}
```
