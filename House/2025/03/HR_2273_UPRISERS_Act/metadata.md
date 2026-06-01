# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2273?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2273
- Title: UPRISERS Act
- Congress: 119
- Bill type: HR
- Bill number: 2273
- Origin chamber: House
- Introduced date: 2025-03-21
- Update date: 2025-12-11T09:06:51Z
- Update date including text: 2025-12-11T09:06:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-21: Introduced in House
- 2025-03-21 - IntroReferral: Introduced in House
- 2025-03-21 - IntroReferral: Introduced in House
- 2025-03-21 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-03-21: Introduced in House

## Actions

- 2025-03-21 - IntroReferral: Introduced in House
- 2025-03-21 - IntroReferral: Introduced in House
- 2025-03-21 - IntroReferral: Referred to the House Committee on the Judiciary.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2273",
    "number": "2273",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "P000048",
        "district": "11",
        "firstName": "August",
        "fullName": "Rep. Pfluger, August [R-TX-11]",
        "lastName": "Pfluger",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "UPRISERS Act",
    "type": "HR",
    "updateDate": "2025-12-11T09:06:51Z",
    "updateDateIncludingText": "2025-12-11T09:06:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-21",
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
          "date": "2025-03-21T20:02:45Z",
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
      "bioguideId": "L000603",
      "district": "8",
      "firstName": "Morgan",
      "fullName": "Rep. Luttrell, Morgan [R-TX-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Luttrell",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "TX"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "MI"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "MN"
    },
    {
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "NC"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "WI"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "NE"
    },
    {
      "bioguideId": "G000601",
      "district": "12",
      "firstName": "Craig",
      "fullName": "Rep. Goldman, Craig A. [R-TX-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "TX"
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
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-12-10",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2273ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2273\nIN THE HOUSE OF REPRESENTATIVES\nMarch 21, 2025 Mr. Pfluger (for himself, Mr. Luttrell , Mr. Bergman , Mr. Stauber , and Mr. Edwards ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo direct the Secretary of State to revoke the visa of any alien admitted to the United States under section 101(a)(15)(F) of the Immigration and Nationality Act who has been convicted of assault in a police officer or an offense related to rioting.\n#### 1. Short title\nThis Act may be cited as the UProot Rioting International Students Engaged in Radical Subversion Act or the UPRISERS Act .\n#### 2. Revocation of student visas for assaulting a police officer and rioting\nThe Secretary of State shall revoke the visa of any alien admitted to the United States under section 101(a)(15)(F), (J), or (M) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(15)(F) , (J), (M)) who has been convicted of\u2014\n**(1)**\nassaulting a police officer; or\n**(2)**\nan offense related to rioting, including\u2014\n**(A)**\ninciting a riot;\n**(B)**\norganizing, promoting, encouraging, participating in, or carrying on a riot;\n**(C)**\ncommitting any act of violence in furtherance of a riot; or\n**(D)**\naiding or abetting any person in inciting or participating in or carrying on a riot or committing any act of violence in furtherance of a riot.\n#### 3. Deportability of student visa holders for assaulting a police officer and rioting\nSection 237(a)(2) of the Immigration and Nationality Act ( 8 U.S.C. 1227(a)(2) ) is amended by adding at the end the following:\n(G) Student visa holders who assault a police officer or rioting Any alien admitted to the United States under section 101(a)(15)(F), (J), or (M) who has been convicted of\u2014 (i) assaulting a police officer; or (ii) an offense related to rioting, including\u2014 (I) inciting a riot; (II) organizing, promoting, encouraging, participating in, or carrying on a riot; (III) committing any act of violence in furtherance of a riot; or (IV) aiding or abetting any person in inciting or participating in or carrying on a riot or committing any act of violence in furtherance of a riot, is deportable. .",
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
        "name": "Immigration",
        "updateDate": "2025-04-01T17:30:19Z"
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
      "date": "2025-03-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2273ih.xml"
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
      "title": "UPRISERS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-01T04:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "UPRISERS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-01T04:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "UProot Rioting International Students Engaged in Radical Subversion Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-01T04:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of State to revoke the visa of any alien admitted to the United States under section 101(a)(15)(F) of the Immigration and Nationality Act who has been convicted of assault in a police officer or an offense related to rioting.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-01T04:18:35Z"
    }
  ]
}
```
