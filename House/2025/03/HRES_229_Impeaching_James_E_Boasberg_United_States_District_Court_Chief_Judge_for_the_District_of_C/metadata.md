# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/229?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/229
- Title: Impeaching James E. Boasberg, United States District Court Chief Judge for the District of Columbia, for high crimes and misdemeanors.
- Congress: 119
- Bill type: HRES
- Bill number: 229
- Origin chamber: House
- Introduced date: 2025-03-18
- Update date: 2026-01-22T09:06:08Z
- Update date including text: 2026-01-22T09:06:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-18: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-03-18 - IntroReferral: Submitted in House
- 2025-03-18 - IntroReferral: Submitted in House
- Latest action: 2025-03-18: Submitted in House

## Actions

- 2025-03-18 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-03-18 - IntroReferral: Submitted in House
- 2025-03-18 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-18",
    "latestAction": {
      "actionDate": "2025-03-18",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/229",
    "number": "229",
    "originChamber": "House",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "G000603",
        "district": "26",
        "firstName": "Brandon",
        "fullName": "Rep. Gill, Brandon [R-TX-26]",
        "lastName": "Gill",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Impeaching James E. Boasberg, United States District Court Chief Judge for the District of Columbia, for high crimes and misdemeanors.",
    "type": "HRES",
    "updateDate": "2026-01-22T09:06:08Z",
    "updateDateIncludingText": "2026-01-22T09:06:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-18",
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
      "actionCode": "H11100",
      "actionDate": "2025-03-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-03-18",
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
          "date": "2025-03-18T16:08:40Z",
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
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "AZ"
    },
    {
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "GA"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "GA"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "AL"
    },
    {
      "bioguideId": "C001116",
      "district": "9",
      "firstName": "Andrew",
      "fullName": "Rep. Clyde, Andrew S. [R-GA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clyde",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "GA"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "CO"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham [R-AZ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "AZ"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "FL"
    },
    {
      "bioguideId": "S001188",
      "district": "3",
      "firstName": "Marlin",
      "fullName": "Rep. Stutzman, Marlin A. [R-IN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Stutzman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "IN"
    },
    {
      "bioguideId": "D000626",
      "district": "8",
      "firstName": "Warren",
      "fullName": "Rep. Davidson, Warren [R-OH-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Davidson",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "OH"
    },
    {
      "bioguideId": "B001316",
      "district": "7",
      "firstName": "Eric",
      "fullName": "Rep. Burlison, Eric [R-MO-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Burlison",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "MO"
    },
    {
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "AZ"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "TX"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "WI"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "NC"
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
      "sponsorshipDate": "2025-03-21",
      "state": "GA"
    },
    {
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "IL"
    },
    {
      "bioguideId": "M001239",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. McGuire, John [R-VA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "McGuire",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "VA"
    },
    {
      "bioguideId": "R000619",
      "district": "6",
      "firstName": "Michael",
      "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Rulli",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "OH"
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
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "TN"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "AZ"
    },
    {
      "bioguideId": "H001086",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harshbarger",
      "party": "R",
      "sponsorshipDate": "2025-12-12",
      "state": "TN"
    },
    {
      "bioguideId": "A000379",
      "district": "4",
      "firstName": "Mark",
      "fullName": "Rep. Alford, Mark [R-MO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Alford",
      "party": "R",
      "sponsorshipDate": "2026-01-21",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres229ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 229\nIN THE HOUSE OF REPRESENTATIVES\nMarch 18, 2025 Mr. Gill of Texas (for himself, Mr. Crane , Mr. Collins , Mr. Carter of Georgia , Mr. Moore of Alabama , and Mr. Clyde ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nImpeaching James E. Boasberg, United States District Court Chief Judge for the District of Columbia, for high crimes and misdemeanors.\nThat James E. Boasberg, Chief Judge, United States Court for the District of Columbia, is impeached for high crimes and misdemeanors, and that the following article of impeachment be exhibited to the United States Senate.\nArticle of impeachment exhibited by the House of Representatives of the United States of America in the name of itself and of the people of the United States of America, against James E. Boasberg, Chief Judge, United States District Court for the District of Columbia, in maintenance and support of its impeachment against him for high crimes and misdemeanors.\n#### ARTICLE I: ABUSE OF POWER\nChief Judge Boasberg, in violation of his oath of office, did knowingly and willfully use his judicial position to advance political gain while interfering with the President's constitutional prerogatives and enforcement of the rule of law.\nThe Constitution provides that the House of Representatives shall have the sole Power of Impeachment and that civil Officers of the United States, including Federal Judges, are subject to impeachment and removal.\nFurther, the separation of powers under the Constitution grants the President broad authority over the executive branch, including authority to protect the nation, as part of his role in ensuring the administration of laws, including the Alien Enemies Act, and policies of the United States.\nThe Alien Enemies Act commits to the President's sole and unreviewable discretion the authority to invoke the provisions of the Act, including the power to determine whether an invasion has taken place. As the Supreme Court has explained, for a court to second-guess a President's determination under the Alien Enemies Act would be assuming the functions of the political agencies of the Government and [i]t is not for [courts] to question the President's determinations under the Alien Enemies Act because [t]hese are matters of political judgement for which judges have neither technical competence nor official responsibility. Ludecke Y. Watkins, 335 U.S. 160(1948). Yet, notwithstanding this binding precedent from the highest court in the land, Chief Judge Boasberg has done exactly what the Supreme Court command not be done, and has illegitimately tried to substitute his own judgement for that of the elected President of the United States, thereby usurping the role of the Executive and unilaterally taking upon himself the power and authority of the President.\nThrough his conduct, in which he violated his oath to the Constitution and duty of impartiality to the people of the United States, Chief Judge Boasberg has abused the powers of his judicial authority, having engaged in actions that prioritize political.gain over the duty of impartiality owed to the public and litigants as follows:\n**(1)**\nChief Judge Boasberg has prevented President Trump from removing aliens associated with Tren de Aragua, a designated Foreign Terrorist Organization from the United States.\n**(2)**\nChief Judge Boasberg required President Trump to turn around planes midair that had aliens associated with Tren de Aragua, a designated Foreign Terrorist Organization.\nThis conduct jeopardizes the safety of the nation, represents an abuse of judicial power, and is detrimental to the orderly functioning of the judiciary. Using the powers of his office, Chief Judge Boasberg has attempted to seize power from the Executive Branch and interfere with the will of the American people.\nIn so doing, Chief Judge Boasberg used the powers of his position to engage in actions that overstep his judicial authority. By making a political decision outside the scope of his judicial duties, he compromised the impartiality of our judicial system and created a constitutional crisis.\nWherefore, Chief Judge Boasberg is guilty of high crimes and misdemeanors and should be removed from office.",
      "versionDate": "2025-03-18",
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
        "updateDate": "2025-03-19T18:37:56Z"
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
      "date": "2025-03-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres229ih.xml"
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
      "title": "Impeaching James E. Boasberg, United States District Court Chief Judge for the District of Columbia, for high crimes and misdemeanors.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-19T09:48:26Z"
    },
    {
      "title": "Impeaching James E. Boasberg, United States District Court Chief Judge for the District of Columbia, for high crimes and misdemeanors.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-19T08:05:49Z"
    }
  ]
}
```
