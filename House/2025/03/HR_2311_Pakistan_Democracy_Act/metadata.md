# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2311?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2311
- Title: Pakistan Democracy Act
- Congress: 119
- Bill type: HR
- Bill number: 2311
- Origin chamber: House
- Introduced date: 2025-03-24
- Update date: 2025-12-13T09:07:05Z
- Update date including text: 2025-12-13T09:07:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-24: Introduced in House
- 2025-03-24 - IntroReferral: Introduced in House
- 2025-03-24 - IntroReferral: Introduced in House
- 2025-03-24 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-24 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-03-24: Introduced in House

## Actions

- 2025-03-24 - IntroReferral: Introduced in House
- 2025-03-24 - IntroReferral: Introduced in House
- 2025-03-24 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-24 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-24",
    "latestAction": {
      "actionDate": "2025-03-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2311",
    "number": "2311",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "W000795",
        "district": "2",
        "firstName": "Joe",
        "fullName": "Rep. Wilson, Joe [R-SC-2]",
        "lastName": "Wilson",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "Pakistan Democracy Act",
    "type": "HR",
    "updateDate": "2025-12-13T09:07:05Z",
    "updateDateIncludingText": "2025-12-13T09:07:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-24",
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
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-24",
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
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-24",
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
          "date": "2025-03-24T16:02:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-03-24T16:02:40Z",
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
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "CA"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "CA"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "IL"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2025-04-17",
      "state": "NY"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "IN"
    },
    {
      "bioguideId": "S001193",
      "district": "14",
      "firstName": "Eric",
      "fullName": "Rep. Swalwell, Eric [D-CA-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Swalwell",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "CA"
    },
    {
      "bioguideId": "O000176",
      "district": "2",
      "firstName": "Johnny",
      "fullName": "Rep. Olszewski, Johnny [D-MD-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Olszewski",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "MD"
    },
    {
      "bioguideId": "C001091",
      "district": "20",
      "firstName": "Joaquin",
      "fullName": "Rep. Castro, Joaquin [D-TX-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Castro",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "TX"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "VA"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-05-06",
      "state": "IL"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "WI"
    },
    {
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-05-09",
      "state": "FL"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "PA"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "MA"
    },
    {
      "bioguideId": "S000522",
      "district": "4",
      "firstName": "Christopher",
      "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "NJ"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "FL"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-12-12",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2311ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2311\nIN THE HOUSE OF REPRESENTATIVES\nMarch 24, 2025 Mr. Wilson of South Carolina (for himself and Mr. Panetta ) introduced the following bill; which was referred to the Committee on Foreign Affairs , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo authorize the imposition of sanctions with respect to certain foreign persons who have knowingly engaged in the wrongful persecution and imprisonment of political opponents in Pakistan, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Pakistan Democracy Act .\n#### 2. Statement of policy\nIt is the policy of the United States to support a democratic Pakistan, including free and fair elections, that is based upon civilian rule, restoration of judicial independence, rule of law, human rights, and due process of law for all of the people of Pakistan.\n#### 3. Determination regarding General Asim Munir\n##### (a) Sanctions\nNot later than 180 days after the date of the enactment of this Act, the Secretary of State, acting in conjunction with the Secretary of the Treasury, shall impose sanctions on General Asim Munir, Chief of Army Staff of Pakistan, the Global Magnitsky Human Rights Accountability Act ( 22 U.S.C. 10101 et seq. ).\n##### (b) Waiver\nThe President may waive subsection (a) if the President certifies to the House Committee on Foreign Affairs, and the Senate Committee on Foreign Relations that\u2014\n**(1)**\nmilitary rule has ended in Pakistan and rule of law and civilian-led democracy has been restored; and\n**(2)**\nall wrongfully detained political detainees have been released from detention.\n#### 4. Authorization of sanctions\n##### (a) Inadmissibility of officials and individuals involved in the wrongful persecution and imprisonment of Imran Khan\n**(1) In general**\nNot later than 180 days after the date of the enactment of this Act, the President shall identify key individuals who are knowingly engaged the wrongful persecution and imprisonment of political detainees in Pakistan including but not limited to former Prime Minister Imran Khan or significantly undermined democracy and furthered military rule for the people of Pakistan including\u2014\n**(A)**\nsuch individuals who have served as a member of the Government or military of Pakistan; and\n**(B)**\nsuch individuals who are serving as an official in a leadership position working on behalf of the Government or military of Pakistan, including law enforcement, intelligence, judicial, or local or municipal government.\n**(2) Ineligibility for visas, admission, or parole**\n**(A) Visas, admission, or parole**\nAn alien with respect to which the President has made an affirmative decision under paragraph (1) shall be\u2014\n**(i)**\ninadmissible to the United States;\n**(ii)**\nineligible to receive a visa or other documentation to enter the United States; and\n**(iii)**\notherwise ineligible to be admitted or paroled into the United States or to receive any other benefit under the Immigration and Nationality Act (8 U.S.C. 1101 et 16 seq.).\n**(B) Current visas revoked**\n**(i) In general**\nThe visa or other entry documentation of any alien described in paragraph (1) is subject to revocation regardless of the issue date of the visa or other entry documentation.\n**(ii) Immediate effect**\nA revocation under subclause (I) shall, in accordance with section 221(i) of the Immigration and Nationality Act ( 8 U.S.C. 1201(i) ) take effect immediately, and cancel any other valid visa or entry documentation that is in the possession of the alien.\n**(3) Briefing**\nNot later than 90 days after the date of the enactment of this Act, the Secretary of State shall brief the appropriate committees of Congress with respect to\u2014\n**(A)**\nany foreign person with respect to which the President has made an affirmative determination under paragraph (1); and\n**(B)**\nthe specific facts that justify each such affirmative determination.\n**(4) Waiver**\nThe President may waive imposition of sanctions under this subsection on a case-by-case basis if the President determines and certifies to the appropriate committees of Congress that\u2014\n**(A)**\nsuch waiver would serve national interests; or\n**(B)**\nthe circumstances which caused the individual to be ineligible have sufficiently changed.\n##### (b) Definitions\nIn this section:\n**(1) Admission; admitted; alien**\nThe terms admission , admitted , and alien have the meanings given such terms in section 101 of the Immigration and Nationality Act ( 8 U.S.C. 1101 ).\n**(2) Appropriate committees of congress**\nThe term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Foreign Affairs, the Committee on the Judiciary, and the Committee on Financial Services of the House of Representatives; and\n**(B)**\nthe Committee on Foreign Relations, the Committee on the Judiciary, and the Committee on Banking, Housing, and Urban Affairs of the Senate.\n**(3) Foreign person**\nThe term foreign person means any individual that is not a United States person.\n**(4) Immediate family members**\nThe term immediate family members has the meaning given the term immediate relatives in section 1151(b)(2)(A)(i) of the Immigration and Nationality Act ( 8 U.S.C. 1151(b)(2)(A)(i) ).\n**(5) Knowingly**\nThe term knowingly , with respect to conduct, a circumstance, or a result, means that a person has actual knowledge, or should have known, of the conduct, the circumstance, or the result.\n**(6) United states person**\nThe term United States person means\u2014\n**(A)**\na United States citizen or an alien lawfully admitted for permanent residence to the United States; or\n**(B)**\nany person within the United States.",
      "versionDate": "2025-03-24",
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
        "name": "International Affairs",
        "updateDate": "2025-05-20T18:24:12Z"
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
      "date": "2025-03-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2311ih.xml"
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
      "title": "Pakistan Democracy Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:33:43Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Pakistan Democracy Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the imposition of sanctions with respect to certain foreign persons who have knowingly engaged in the wrongful persecution and imprisonment of political opponents in Pakistan, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T13:18:46Z"
    }
  ]
}
```
