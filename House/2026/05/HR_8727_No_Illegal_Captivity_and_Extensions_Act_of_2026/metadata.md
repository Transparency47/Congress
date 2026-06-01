# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8727?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8727
- Title: No Illegal Captivity and Extensions Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8727
- Origin chamber: House
- Introduced date: 2026-05-11
- Update date: 2026-05-19T22:30:59Z
- Update date including text: 2026-05-19T22:30:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-11: Introduced in House
- 2026-05-11 - IntroReferral: Introduced in House
- 2026-05-11 - IntroReferral: Introduced in House
- 2026-05-11 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-05-11: Introduced in House

## Actions

- 2026-05-11 - IntroReferral: Introduced in House
- 2026-05-11 - IntroReferral: Introduced in House
- 2026-05-11 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-11",
    "latestAction": {
      "actionDate": "2026-05-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8727",
    "number": "8727",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "F000476",
        "district": "10",
        "firstName": "Maxwell",
        "fullName": "Rep. Frost, Maxwell [D-FL-10]",
        "lastName": "Frost",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "No Illegal Captivity and Extensions Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-19T22:30:59Z",
    "updateDateIncludingText": "2026-05-19T22:30:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-11",
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
      "actionDate": "2026-05-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-11",
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
          "date": "2026-05-11T14:31:40Z",
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
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "CA"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "AZ"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8727ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8727\nIN THE HOUSE OF REPRESENTATIVES\nMay 11, 2026 Mr. Frost (for himself, Mr. Garcia of California , Ms. Ansari , and Mr. Bell ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Immigration and Nationality Act to eliminate immigration detainers.\n#### 1. Short title\nThis Act may be cited as the No Illegal Captivity and Extensions Act of 2026 or as the NICE Act of 2026 .\n#### 2. Elimination of immigration detainers\n##### (a) Apprehension and detention of aliens\nSection 236 of the Immigration and Nationality Act ( 8 U.S.C. 1226(c) ) is amended by striking paragraph (3).\n##### (b) Detainer of aliens for violation of controlled substances laws\nSection 287 of the Immigration and Nationality Act ( 8 U.S.C. 1357 ) is amended by striking subsection (d).\n##### (c) Intergovernmental service agreements\nSection 103(a)(11)(B) of the Immigration and Nationality Act ( 8 U.S.C. 1103(a)(11)(B) ) is amended by inserting before the period at the end the following: , except that the Secretary may not impose, as a condition of any such agreement, that any other party enforce a detainer or hold issued by the Secretary .\n##### (d) General prohibition\nNotwithstanding any other provision of law, the Secretary of Homeland Security may not issue or enforce any detainer or hold under the immigration laws, including through the use of an intergovernmental service agreement, basic ordering agreement, or any other written or informal instrument of understanding with any Federal, State, or local law enforcement agency.",
      "versionDate": "2026-05-11",
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
        "updateDate": "2026-05-19T22:30:59Z"
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
      "date": "2026-05-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8727ih.xml"
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
      "title": "No Illegal Captivity and Extensions Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-12T08:23:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Illegal Captivity and Extensions Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-12T08:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Immigration and Nationality Act to eliminate immigration detainers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-12T08:18:30Z"
    }
  ]
}
```
