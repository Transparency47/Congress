# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1928?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1928
- Title: Sanctuary City Accountability Act
- Congress: 119
- Bill type: HR
- Bill number: 1928
- Origin chamber: House
- Introduced date: 2025-03-06
- Update date: 2026-05-22T08:08:37Z
- Update date including text: 2026-05-22T08:08:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-06: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-03-06: Introduced in House

## Actions

- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-06",
    "latestAction": {
      "actionDate": "2025-03-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1928",
    "number": "1928",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "I000056",
        "district": "48",
        "firstName": "Darrell",
        "fullName": "Rep. Issa, Darrell [R-CA-48]",
        "lastName": "Issa",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "Sanctuary City Accountability Act",
    "type": "HR",
    "updateDate": "2026-05-22T08:08:37Z",
    "updateDateIncludingText": "2026-05-22T08:08:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-06",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-06",
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
          "date": "2025-03-06T14:07:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "TX"
    },
    {
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "AZ"
    },
    {
      "bioguideId": "G000589",
      "district": "5",
      "firstName": "Lance",
      "fullName": "Rep. Gooden, Lance [R-TX-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gooden",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "TX"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "FL"
    },
    {
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "IA"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "OK"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-05-21",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1928ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1928\nIN THE HOUSE OF REPRESENTATIVES\nMarch 6, 2025 Mr. Issa (for himself, Mr. Gill of Texas , Mr. Crane , Mr. Gooden , Mr. Haridopolos , and Mr. Feenstra ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo authorize private enforcement of immigration laws, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Sanctuary City Accountability Act .\n#### 2. Private enforcement of immigration laws\nTitle I of the Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ) is amended by adding at the end the following new section:\n107. Private right of action (a) In general Any individual who is a national of the United States may bring a civil action in an appropriate district court of the United States against a sanctuary jurisdiction in which an alien was located if that alien commits a crime against that individual, or an immediate family member of that individual, in the sanctuary jurisdiction, or in any other jurisdiction to which the alien later relocates, for such injunctive relief or compensatory damages as may be appropriate. (b) Limitation on liability A unit of local government may not be held liable under this section for enforcing or implementing a law, ordinance, regulation, resolution, policy, or other practice imposed by the State in which the unit of local government is located. (c) Sanctuary jurisdiction defined In this section, the term sanctuary jurisdiction means any State or unit of local government that has laws, ordinances, regulations, resolutions, policies, or other practices that obstruct immigration enforcement and shield criminals from U.S. Immigration and Customs Enforcement, including by\u2014 (1) refusing to or prohibiting agencies from complying with U.S. Immigration and Customs Enforcement detainers; (2) imposing unreasonable conditions on U.S. Immigration and Customs Enforcement detainer compliance; (3) denying U.S. Immigration and Customs Enforcement access to interview incarcerated aliens; or (4) otherwise impeding communication or information exchanges between the jurisdiction\u2019s personnel and Federal immigration officers. .",
      "versionDate": "2025-03-06",
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
        "name": "Immigration",
        "updateDate": "2025-03-26T18:12:20Z"
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
      "date": "2025-03-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1928ih.xml"
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
      "title": "Sanctuary City Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-26T11:53:19Z"
    },
    {
      "title": "Sanctuary City Accountability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-26T11:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize private enforcement of immigration laws, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-26T11:48:20Z"
    }
  ]
}
```
