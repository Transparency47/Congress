# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1536?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1536
- Title: PIFAA
- Congress: 119
- Bill type: HR
- Bill number: 1536
- Origin chamber: House
- Introduced date: 2025-02-24
- Update date: 2026-05-03T23:19:16Z
- Update date including text: 2026-05-03T23:19:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-24: Introduced in House
- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-02-24 - Committee: Referred to the Subcommittee on Aviation.
- Latest action: 2025-02-24: Introduced in House

## Actions

- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-02-24 - Committee: Referred to the Subcommittee on Aviation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-24",
    "latestAction": {
      "actionDate": "2025-02-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1536",
    "number": "1536",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "M001219",
        "district": "",
        "firstName": "James",
        "fullName": "Del. Moylan, James C. [R-GU-At Large]",
        "lastName": "Moylan",
        "party": "R",
        "state": "GU"
      }
    ],
    "title": "PIFAA",
    "type": "HR",
    "updateDate": "2026-05-03T23:19:16Z",
    "updateDateIncludingText": "2026-05-03T23:19:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-24",
      "committees": {
        "item": {
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Aviation.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-24",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-24",
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
          "date": "2025-02-24T17:03:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-24T21:46:32Z",
              "name": "Referred to"
            }
          },
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "K000404",
      "district": "0",
      "firstName": "Kimberlyn",
      "fullName": "Del. King-Hinds, Kimberlyn [R-MP-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "King-Hinds",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "MP"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1536ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1536\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 24, 2025 Mr. Moylan (for himself and Ms. King-Hinds ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo allow certain foreign air carriers to stop in Guam or the Northern Mariana Islands in the course of transportation of passengers or cargo in either direction between a place in the United States and a place outside the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Pacific Island Flight Alternatives Act of 2025 or PIFAA .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nLimited air competition has made flights from Guam to the Commonwealth of Northern Mariana Islands or to Hawaii exceedingly expensive.\n**(2)**\nThe airports of Antonio B. Won Pat Guam International Airport (IATA: GUM), Francisco C. Ada Saipan International Airport (IATA: SPN), Francisco Manglona Borja Tinian International Airport (IATA: TIQ), and Benjamin Taisacan Manglona Rota International Airport (IATA: ROP) rely on foreign air carriers for travel.\n**(3)**\nThe nations of Japan, Philippines, and the Republic of Korea have been critical allies for the United States within the Indo-Pacific region.\n**(4)**\nThe nations of Japan, Philippines, and the Republic of Korea and the air carriers of such nations have been vital in supplementing deficiencies of United States air carriers when flying between the United States and other Pacific Islands.\n#### 3. Air commerce in Guam and Northern Mariana Islands\nSection 41703 of title 49, United States Code, is amended by adding at the end the following:\n(f) Air commerce in Guam and Northern Mariana Islands (1) In general For purposes of subsection (c), passengers or cargo added to or removed from an authorized Pacific aircraft at a place in Guam or the Northern Mariana Islands in the course of transportation of such passengers or cargo in either direction between a place in the United States and a place outside the United States shall not be deemed to have broken the international journey of such authorized Pacific aircraft. (2) Authorized Pacific aircraft In this subsection, the term authorized Pacific aircraft means an aircraft registered to a foreign air carrier from Japan, Philippines, or the Republic of Korea that holds a permit under section 41302. .",
      "versionDate": "2025-02-24",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-03-21T15:51:53Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-24",
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
          "measure-id": "id119hr1536",
          "measure-number": "1536",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-24",
          "originChamber": "HOUSE",
          "update-date": "2026-05-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1536v00",
            "update-date": "2026-05-03"
          },
          "action-date": "2025-02-24",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Pacific Island Flight Alternatives Act of 2025 or\u00a0PIFAA</strong></p><p>This bill allows authorized foreign aircraft to pick up and drop off\u00a0passengers and cargo in Guam or the Northern\u00a0Mariana Islands on international flights to or from other places in the United States. Authorized aircraft are those registered to a foreign air carrier from Japan, the Philippines, or South Korea.</p><p>Current law prohibits foreign air carriers from transporting passengers or cargo between places in the United States, with exceptions.</p><p>The bill deems that passengers or cargo that are added to or removed from authorized\u00a0foreign\u00a0aircraft in Guam or the Northern\u00a0Mariana Islands on a flight that is traveling between another place in the United States and an international location have not broken the international journey, thus allowing authorized foreign aircraft to transport passengers and cargo between Guam or the Northern\u00a0Mariana Islands and other places in the United States on such flights.</p>"
        },
        "title": "PIFAA"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1536.xml",
    "summary": {
      "actionDate": "2025-02-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Pacific Island Flight Alternatives Act of 2025 or\u00a0PIFAA</strong></p><p>This bill allows authorized foreign aircraft to pick up and drop off\u00a0passengers and cargo in Guam or the Northern\u00a0Mariana Islands on international flights to or from other places in the United States. Authorized aircraft are those registered to a foreign air carrier from Japan, the Philippines, or South Korea.</p><p>Current law prohibits foreign air carriers from transporting passengers or cargo between places in the United States, with exceptions.</p><p>The bill deems that passengers or cargo that are added to or removed from authorized\u00a0foreign\u00a0aircraft in Guam or the Northern\u00a0Mariana Islands on a flight that is traveling between another place in the United States and an international location have not broken the international journey, thus allowing authorized foreign aircraft to transport passengers and cargo between Guam or the Northern\u00a0Mariana Islands and other places in the United States on such flights.</p>",
      "updateDate": "2026-05-03",
      "versionCode": "id119hr1536"
    },
    "title": "PIFAA"
  },
  "summaries": [
    {
      "actionDate": "2025-02-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Pacific Island Flight Alternatives Act of 2025 or\u00a0PIFAA</strong></p><p>This bill allows authorized foreign aircraft to pick up and drop off\u00a0passengers and cargo in Guam or the Northern\u00a0Mariana Islands on international flights to or from other places in the United States. Authorized aircraft are those registered to a foreign air carrier from Japan, the Philippines, or South Korea.</p><p>Current law prohibits foreign air carriers from transporting passengers or cargo between places in the United States, with exceptions.</p><p>The bill deems that passengers or cargo that are added to or removed from authorized\u00a0foreign\u00a0aircraft in Guam or the Northern\u00a0Mariana Islands on a flight that is traveling between another place in the United States and an international location have not broken the international journey, thus allowing authorized foreign aircraft to transport passengers and cargo between Guam or the Northern\u00a0Mariana Islands and other places in the United States on such flights.</p>",
      "updateDate": "2026-05-03",
      "versionCode": "id119hr1536"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1536ih.xml"
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
      "title": "PIFAA",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-20T12:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PIFAA",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T12:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Pacific Island Flight Alternatives Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T12:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To allow certain foreign air carriers to stop in Guam or the Northern Mariana Islands in the course of transportation of passengers or cargo in either direction between a place in the United States and a place outside the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-20T12:18:39Z"
    }
  ]
}
```
