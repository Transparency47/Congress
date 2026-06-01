# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4119?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4119
- Title: Polisario Front Terrorist Designation Act
- Congress: 119
- Bill type: HR
- Bill number: 4119
- Origin chamber: House
- Introduced date: 2025-06-24
- Update date: 2026-05-30T08:05:38Z
- Update date including text: 2026-05-30T08:05:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-24: Introduced in House
- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-24 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-06-24: Introduced in House

## Actions

- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Introduced in House
- 2025-06-24 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-24 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-24",
    "latestAction": {
      "actionDate": "2025-06-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4119",
    "number": "4119",
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
    "title": "Polisario Front Terrorist Designation Act",
    "type": "HR",
    "updateDate": "2026-05-30T08:05:38Z",
    "updateDateIncludingText": "2026-05-30T08:05:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-24",
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
      "actionDate": "2025-06-24",
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
      "actionDate": "2025-06-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-24",
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
          "date": "2025-06-24T14:04:25Z",
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
          "date": "2025-06-24T14:04:20Z",
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
      "sponsorshipDate": "2025-06-24",
      "state": "CA"
    },
    {
      "bioguideId": "D000600",
      "district": "26",
      "firstName": "Mario",
      "fullName": "Rep. Diaz-Balart, Mario [R-FL-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Diaz-Balart",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "FL"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "IN"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "FL"
    },
    {
      "bioguideId": "G000589",
      "district": "5",
      "firstName": "Lance",
      "fullName": "Rep. Gooden, Lance [R-TX-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gooden",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
      "state": "TX"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2026-02-13",
      "state": "NC"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "IA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "NE"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2026-03-09",
      "state": "NY"
    },
    {
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "NY"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2026-04-06",
      "state": "FL"
    },
    {
      "bioguideId": "M001236",
      "district": "14",
      "firstName": "Tim",
      "fullName": "Rep. Moore, Tim [R-NC-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "NC"
    },
    {
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "False",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4119ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4119\nIN THE HOUSE OF REPRESENTATIVES\nJune 24, 2025 Mr. Wilson of South Carolina (for himself and Mr. Panetta ) introduced the following bill; which was referred to the Committee on Foreign Affairs , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo provide for the imposition of sanctions with respect to the Polisario Front, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Polisario Front Terrorist Designation Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe Polisario Front, founded in 1973, is a separatist group operating primarily in Western Sahara and the Tindouf region of Algeria, seeking independence for Western Sahara from Moroccan sovereignty.\n**(2)**\nThe Polisario Front has a documented history of ideological and operational ties with Iran, a state sponsor of terrorism, dating back at least to 1980, when Polisario fighters publicly posed with portraits of Ayatollah Ruhollah Khomeini in a bid to attract revolutionary credibility and Iranian patronage.\n**(3)**\nAccording to reporting by Jeune Afrique, 3 Hezbollah officers served as trainers in the Tindouf camps in 2018. One of the named trainers, since killed in a November 2023 Israeli airstrike in Syria, had previously been sanctioned by the United States for orchestrating the 2007 Karbala raid in Iraq that killed 5 American soldiers.\n**(4)**\nIran\u2019s support has reportedly advanced from training to the provision of lethal hardware. In a 2022 livestream, Polisario Interior Minister Omar Mansour stated that his fighters were training on assembling and operating armed drones . A year later, images disseminated via Polisario-controlled social media channels showed Iranian-type munitions, as confirmed by open-source weapons researchers.\n**(5)**\nThe Washington Post reported in April 2025 that Iran has trained Polisario Front fighters and provided them with unmanned aerial vehicles (UAVs), deepening concerns about the group's growing capabilities and external sponsorship.\n**(6)**\nThe Syrian wing of the PKK, a designated terrorist organization, took part in the front's meeting called Sahrawi Solidarity Summit in the Sahrawi camps on January 4\u20137 2025.\n#### 3. Report\nNot later than 180 days after the date of the enactment of this Act, the Secretary of State shall submit to the appropriate Congressional committees a report on the Polisario Front to include the following:\n**(1)**\nA description of the Polisario Front\u2019s leadership, military operations, and foreign sponsorship.\n**(2)**\nA description of the Polisario Front\u2019s relationships, support, funding, and associations with Iran and Russia.\n**(3)**\nA description of the Polisario Front\u2019s relationships, support, funding and associations with Foreign Terrorist Organizations Hezbollah, the IRGC, and the PKK.\n**(4)**\nA description and analysis of whether the Polisario Front has ever intentionally attacked civilian targets.\n#### 4. Determinations with respect to the imposition of sanctions against the Polisario Front\n##### (a) Determinations by the Secretary of State\nNot later than 90 days after the date of the enactment of this Act, the Secretary of State shall submit to the appropriate Congressional committees a determination, including a detailed justification, of whether the Polisario Front meets the criteria for\u2014\n**(1)**\ndesignation as a foreign terrorist organization under section 219 of the Immigration and Nationality Act ( 8 U.S.C. 1189 ); and\n**(2)**\nimposition of sanctions under section 1263 of the Global Magnitsky Human Rights Accountability Act (subtitle F of title XII of Public Law 114\u2013328 ; 22 U.S.C. 2656 note).\n##### (b) Determination by the Secretary of the Treasury\nNot later than 90 days after the date of the enactment of this Act, the Secretary of the Treasury shall submit to the appropriate Congressional committees a determination, including a detailed justification, of whether the Polisario Front meets the criteria for the imposition of sanctions under Executive Order 13224 ( 50 U.S.C. 1701 ).\n##### (c) Form\nThe determinations required by subsections (a) and (b) shall be submitted in unclassified form, but may include a classified annex.\n#### 5. Waiver\nThe designations and sanctions described in section (4) of this bill may be waived by the President if it is determined that the Polisario Front is engaged in good faith negotiations to implement the autonomy plan for the Western Sahara put forward by the Kingdom of Morocco and submitted to the UN Security Council in 2007, which proposes granting the Sahrawi people a high degree of self-governance within a framework of Moroccan sovereignty.",
      "versionDate": "2025-06-24",
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
        "updateDate": "2025-07-17T22:26:18Z"
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
      "date": "2025-06-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4119ih.xml"
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
      "title": "Polisario Front Terrorist Designation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-09T04:23:19Z"
    },
    {
      "title": "Polisario Front Terrorist Designation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-09T04:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for the imposition of sanctions with respect to the Polisario Front, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-09T04:18:25Z"
    }
  ]
}
```
