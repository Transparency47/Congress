# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/145?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/145
- Title: Impeaching Paul Adam Engelmayer, United States District Court Judge for the Southern District of New York, for high crimes and misdemeanors.
- Congress: 119
- Bill type: HRES
- Bill number: 145
- Origin chamber: House
- Introduced date: 2025-02-21
- Update date: 2025-03-26T08:06:41Z
- Update date including text: 2025-03-26T08:06:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-21: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-02-21 - Committee: Submitted in House
- Latest action: 2025-02-21: Submitted in House

## Actions

- 2025-02-21 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-02-21 - Committee: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-21",
    "latestAction": {
      "actionDate": "2025-02-21",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/145",
    "number": "145",
    "originChamber": "House",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "C001132",
        "district": "2",
        "firstName": "Elijah",
        "fullName": "Rep. Crane, Elijah [R-AZ-2]",
        "lastName": "Crane",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Impeaching Paul Adam Engelmayer, United States District Court Judge for the Southern District of New York, for high crimes and misdemeanors.",
    "type": "HRES",
    "updateDate": "2025-03-26T08:06:41Z",
    "updateDateIncludingText": "2025-03-26T08:06:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-21",
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
      "actionCode": "H12100",
      "actionDate": "2025-02-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
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
          "date": "2025-02-21T20:32:45Z",
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
      "bioguideId": "D000626",
      "district": "8",
      "firstName": "Warren",
      "fullName": "Rep. Davidson, Warren [R-OH-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Davidson",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "OH"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham [R-AZ-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "AZ"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "FL"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "TN"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "CO"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "TX"
    },
    {
      "bioguideId": "C001116",
      "district": "9",
      "firstName": "Andrew",
      "fullName": "Rep. Clyde, Andrew S. [R-GA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Clyde",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "GA"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "OK"
    },
    {
      "bioguideId": "B001316",
      "district": "7",
      "firstName": "Eric",
      "fullName": "Rep. Burlison, Eric [R-MO-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Burlison",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "MO"
    },
    {
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "GA"
    },
    {
      "bioguideId": "G000596",
      "district": "14",
      "firstName": "Marjorie",
      "fullName": "Rep. Greene, Marjorie Taylor [R-GA-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Greene",
      "middleName": "Taylor",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "GA"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres145ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 145\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 21, 2025 Mr. Crane (for himself, Mr. Davidson , Mr. Hamadeh of Arizona , Mrs. Luna , and Mr. Ogles ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nImpeaching Paul Adam Engelmayer, United States District Court Judge for the Southern District of New York, for high crimes and misdemeanors.\nThat Paul Adam Engelmayer, United States District Court Judge for the Southern District of New York, is impeached for high crimes and misdemeanors, and that the following article of impeachment be exhibited to the United States Senate:\nArticle of impeachment exhibited by the House of Representatives of the United States of America in the name of itself and of the people of the United States of America, against Paul Adam Engelmayer, United States District Court Judge for the Southern District of New York, in maintenance and support of its impeachment against him for high crimes and misdemeanors.\n#### Article I: Abuse of power\nJudge Paul Engelmayer, in violation of his oath of office, did knowingly and willfully use his judicial position to advance personal interests and political gain.\nThe Constitution provides that the House of Representatives shall have the sole Power of Impeachment and that civil Officers of the United States , including Federal judges, are subject to impeachment and removal.\nFurther, the separation of powers under the Constitution grants the President broad authority over the executive branch, including direct control and access to departments, as part of his role in ensuring the administration of laws and policies of the United States.\nIn his conduct of the office of United States District Court Judge, in which he violated his oath to the Constitution and duty of impartiality to the people of the United States, Paul A. Engelmayer has abused the powers of his judicial authority, having engaged in actions that prioritize personal and political affiliations over the duty of impartiality owed to the public and litigants as follows:\n**(1)**\nJudge Engelmayer restrained President Trump and Secretary Bessent from granting access to any Department of the Treasury record, payment systems, or any other data systems maintained by the Department of the Treasury containing personally identifiable information or confidential financial information of payees; and\n**(2)**\nJudge Engelmayer restrained President Trump and Secretary Bessent from granting access to all political appointees, special Government employees, and Government employees detailed from another Federal agency, to any Department of the Treasury payment record, payment systems, or any other data systems maintained by the Department of the Treasury containing personally identifiable information.\nThis conduct has resulted in apparent bias and favoritism, representing an abuse of judicial power and is detrimental to the orderly functioning of the judiciary. Using the powers of his high office, Judge Engelmayer interfered with the will of the people.\nIn so doing, Judge Engelmayer used the powers of his position to engage in actions that overstep his judicial authority. By making a political decision outside the scope of his legal duties, he compromised the impartiality of our judicial system.\nWherefore, Judge Engelmayer is guilty of high crimes and misdemeanors and should be removed from office.",
      "versionDate": "2025-02-21",
      "versionType": "IH"
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
        "name": "Law",
        "updateDate": "2025-02-24T19:33:09Z"
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
      "date": "2025-02-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres145ih.xml"
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
      "title": "Impeaching Paul Adam Engelmayer, United States District Court Judge for the Southern District of New York, for high crimes and misdemeanors.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T09:48:40Z"
    },
    {
      "title": "Impeaching Paul Adam Engelmayer, United States District Court Judge for the Southern District of New York, for high crimes and misdemeanors.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-22T09:05:59Z"
    }
  ]
}
```
