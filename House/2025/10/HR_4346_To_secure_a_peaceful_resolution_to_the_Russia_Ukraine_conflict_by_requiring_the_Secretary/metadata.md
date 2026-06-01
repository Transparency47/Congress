# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4346?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4346
- Title: PEACE Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4346
- Origin chamber: House
- Introduced date: 2025-07-10
- Update date: 2026-05-12T20:20:22Z
- Update date including text: 2026-05-12T20:20:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-10: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-07-22 - Committee: Committee Consideration and Mark-up Session Held
- 2025-07-22 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 53 - 1.
- 2025-10-03 - Calendars: Placed on the Union Calendar, Calendar No. 277.
- 2025-10-03 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-324.
- 2025-10-03 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-324.
- Latest action: 2025-07-10: Introduced in House

## Actions

- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-07-22 - Committee: Committee Consideration and Mark-up Session Held
- 2025-07-22 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 53 - 1.
- 2025-10-03 - Calendars: Placed on the Union Calendar, Calendar No. 277.
- 2025-10-03 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-324.
- 2025-10-03 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-324.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4346",
    "number": "4346",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "N000193",
        "district": "3",
        "firstName": "Zachary",
        "fullName": "Rep. Nunn, Zachary [R-IA-3]",
        "lastName": "Nunn",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "PEACE Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-12T20:20:22Z",
    "updateDateIncludingText": "2026-05-12T20:20:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H12410",
      "actionDate": "2025-10-03",
      "calendarNumber": {
        "calendar": "U00277"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 277.",
      "type": "Calendars"
    },
    {
      "actionCode": "H12200",
      "actionDate": "2025-10-03",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Reported (Amended) by the Committee on Financial Services. H. Rept. 119-324.",
      "type": "Committee"
    },
    {
      "actionCode": "5000",
      "actionDate": "2025-10-03",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Reported (Amended) by the Committee on Financial Services. H. Rept. 119-324.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-22",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 53 - 1.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-22",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-10",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
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
        "item": [
          {
            "date": "2025-10-03T20:03:47Z",
            "name": "Reported By"
          },
          {
            "date": "2025-07-22T15:56:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-07-10T15:02:00Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "NJ"
    },
    {
      "bioguideId": "B001321",
      "district": "7",
      "firstName": "Tom",
      "fullName": "Rep. Barrett, Tom [R-MI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrett",
      "party": "R",
      "sponsorshipDate": "2025-07-14",
      "state": "MI"
    },
    {
      "bioguideId": "C001136",
      "district": "3",
      "firstName": "Herbert",
      "fullName": "Rep. Conaway, Herbert C. [D-NJ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Conaway",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "NJ"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4346ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4346\nIN THE HOUSE OF REPRESENTATIVES\nJuly 10, 2025 Mr. Nunn of Iowa (for himself and Mr. Gottheimer ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo secure a peaceful resolution to the Russia-Ukraine conflict by requiring the Secretary of the Treasury to prohibit, or impose strict conditions on, the opening or maintaining in the United States of a correspondent account or a payable-through account by certain foreign financial institutions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Preventing the Escalation of Armed Conflict in Europe Act of 2025 or the PEACE Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nDuring the night of March 6\u20137, 2025, only one week after the President called for peace between Russia and Ukraine, the Russian military bombarded Ukrainian energy infrastructure and civilian residences.\n**(2)**\nDTEK, a Ukrainian gas producer, noted that the assault represented the sixth Russian attack on its Odesa facilities in just the preceding two and a half weeks.\n**(3)**\nOn March 7, 2025, the President published the following statement: Based on the fact that Russia is absolutely pounding Ukraine on the battlefield right now, I am strongly considering large scale Banking Sanctions, Sanctions, and Tariffs on Russia until a Cease Fire and FINAL SETTLEMENT AGREEMENT ON PEACE IS REACHED. To Russia and Ukraine, get to the table right now, before it is too late. .\n**(4)**\nDespite the President\u2019s calls for a peace settlement, Russia has continued to assault Ukraine, including an April 4 missile attack on Kryvyi Rih that killed 20 people and an April 13 strike on Sumy resulting in 35 deaths.\n**(5)**\nOn May 25, 2025, Russia launched its largest aerial attack of the war, deploying hundreds of drones and ballistic missiles throughout Ukrainian territory.\n**(6)**\nOn May 27, 2025, the President posted on social media with reference to Russian leader Vladimir Putin: He\u2019s playing with fire! .\n**(7)**\nHours after a July 3, 2025, call between the President and Putin, Russia carried out its largest-yet aerial assault of the war against Kyiv. Less than one week later, following remarks by the President at a Cabinet meeting criticizing Putin, Russia launched an even more expansive drone strike against Ukrainian targets.\n#### 3. Sanctions with respect to the Russian Federation\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, the Secretary of the Treasury shall prescribe regulations to prohibit, or impose strict conditions on, the opening or maintaining in the United States of a correspondent account or a payable-through account by a foreign financial institution that knowingly provides significant financial services to\u2014\n**(1)**\nany foreign person designated for the imposition of sanctions with respect to the Russian Federation under\u2014\n**(A)**\nExecutive Orders 13660, 13661, 13662, 13685, or 14024; or\n**(B)**\ntitle II of the Countering America\u2019s Adversaries through Sanctions Act ( Public Law 114\u201344 ) or an amendment made by that title;\n**(2)**\na foreign financial institution subject to the prohibitions of Directive 2 under Executive Order 14024;\n**(3)**\nan entity listed in Annex 1 of Directive 3 under Executive Order 14024; or\n**(4)**\nany foreign person that the Secretary finds operates in the energy sector of the Russian Federation.\n##### (b) Penalties\n**(1) Civil penalty**\nA person who violates, attempts to violate, conspires to violate, or causes a violation of regulations prescribed under this subsection shall be subject to a civil penalty in an amount not to exceed the greater of\u2014\n**(A)**\n$377,700; or\n**(B)**\nan amount that is twice the amount of the transaction that is the basis of the violation with respect to which the penalty is imposed.\n**(2) Criminal penalty**\nA person who willfully commits, willfully attempts to commit, or willfully conspires to commit, or aids or abets in the commission of, a violation of regulations prescribed under this subsection shall, upon conviction, be fined not more than $1,000,000, or if a natural person, may be imprisoned for not more than 20 years, or both.\n#### 4. Determination required\nNot later than 90 days after the date of enactment of this Act, the Secretary of the Treasury shall submit a report to Committee on Financial Services of the House of Representatives and the Committee on Banking, Housing, and Urban Affairs of the Senate determining whether the following are foreign persons described under section 3(a)(4):\n**(1)**\nGazprom.\n**(2)**\nRosneft.\n**(3)**\nLukoil.\n#### 5. Waiver\nWith respect to a foreign financial institution, the President may waive the requirements of section 3(a) for not more than 180 days at a time upon reporting to Congress that\u2014\n**(1)**\nthe waiver advances the objective of resolving the national emergency described in any Executive Order listed under section 3(a)(1); or\n**(2)**\nthe waiver is important to the national interest of the United States, provided that the President includes a detailed explanation of the reasons therefor.\n#### 6. Termination\nThis Act shall have no force or effect on the earlier of\u2014\n**(1)**\n30 days after the date that the President reports to Congress that the Russian Federation has ceased destabilizing activities with respect to the sovereignty and territorial integrity of Ukraine; or\n**(2)**\nthe date that is 5 years after the date of the enactment of this Act.",
      "versionDate": "2025-07-10",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4346rh.xml",
      "text": "IB\nUnion Calendar No. 277\n119th CONGRESS\n1st Session\nH. R. 4346\n[Report No. 119\u2013324]\nIN THE HOUSE OF REPRESENTATIVES\nJuly 10, 2025 Mr. Nunn of Iowa (for himself and Mr. Gottheimer ) introduced the following bill; which was referred to the Committee on Financial Services\nOctober 3, 2025 Additional sponsors: Mr. Barrett , Mr. Conaway , and Mr. Suozzi\nOctober 3, 2025 Reported with an amendment, committed to the Committee of the Whole House on the State of the Union, and ordered to be printed Strike out all after the enacting clause and insert the part printed in italic For text of introduced bill, see copy of bill as introduced on July 10, 2025\nA BILL\nTo secure a peaceful resolution to the Russia-Ukraine conflict by requiring the Secretary of the Treasury to prohibit, or impose strict conditions on, the opening or maintaining in the United States of a correspondent account or a payable-through account by certain foreign financial institutions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Preventing the Escalation of Armed Conflict in Europe Act of 2025 or the PEACE Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nDuring the night of March 6-7, 2025, only one week after the President called for peace between Russia and Ukraine, the Russian military bombarded Ukrainian energy infrastructure and civilian residences.\n**(2)**\nDTEK, a Ukrainian gas producer, noted that the assault represented the sixth Russian attack on its Odesa facilities in just the preceding two and a half weeks.\n**(3)**\nOn March 7, 2025, the President published the following statement: Based on the fact that Russia is absolutely pounding Ukraine on the battlefield right now, I am strongly considering large scale Banking Sanctions, Sanctions, and Tariffs on Russia until a Cease Fire and FINAL SETTLEMENT AGREEMENT ON PEACE IS REACHED. To Russia and Ukraine, get to the table right now, before it is too late. .\n**(4)**\nDespite the President\u2019s calls for a peace settlement, Russia has continued to assault Ukraine, including an April 4 missile attack on Kryvyi Rih that killed 20 people and an April 13 strike on Sumy resulting in 35 deaths.\n**(5)**\nOn May 25, 2025, Russia launched its largest aerial attack of the war, deploying hundreds of drones and ballistic missiles throughout Ukrainian territory.\n**(6)**\nOn May 27, 2025, the President posted on social media with reference to Russian leader Vladimir Putin: He\u2019s playing with fire! .\n**(7)**\nHours after a July 3, 2025 call between the President and Putin, Russia carried out its largest-yet aerial assault of the war against Kyiv. Less than one week later, following remarks by the President at a Cabinet meeting criticizing Putin, Russia launched an even more expansive drone strike against Ukrainian targets.\n**(8)**\nOn July 14, 2025, the President reiterated his displeasure with Putin and Moscow\u2019s obstruction of the peace process. I speak to [Putin] a lot about getting this thing done, said the President while announcing new weapons deliveries for Ukraine. And I always hang up and say, Well, that was a nice phone call . And then missiles are launched into Kyiv or some other city. The President continued, Ultimately talk doesn\u2019t talk. It\u2019s got to be action. It\u2019s got to be results. .\n#### 3. Sanctions with respect to the Russian Federation\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, the Secretary of the Treasury shall prescribe regulations to prohibit, or impose strict conditions on, the opening or maintaining in the United States of a correspondent account or a payable-through account by a foreign financial institution that knowingly provides significant financial services to\u2014\n**(1)**\nany foreign person designated for the imposition of sanctions with respect to the Russian Federation under\u2014\n**(A)**\nExecutive Order 14024; or\n**(B)**\ntitle II of the Countering America\u2019s Adversaries through Sanctions Act ( Public Law 115\u201344 ) or an amendment made by that title;\n**(2)**\na foreign financial institution subject to the prohibitions of Directive 2 under Executive Order 14024;\n**(3)**\nan entity listed in Annex 1 of Directive 3 under Executive Order 14024; or\n**(4)**\nany foreign person that the Secretary finds operates in the energy sector of the Russian Federation.\n##### (b) Penalties\n**(1) Civil penalty**\nA person who violates, attempts to violate, conspires to violate, or causes a violation of regulations prescribed under this subsection shall be subject to a civil penalty in an amount not to exceed the greater of\u2014\n**(A)**\n$377,700; or\n**(B)**\nan amount that is twice the amount of the transaction that is the basis of the violation with respect to which the penalty is imposed.\n**(2) Criminal penalty**\nA person who willfully commits, willfully attempts to commit, or willfully conspires to commit, or aids or abets in the commission of, a violation of regulations prescribed under this subsection shall, upon conviction, be fined not more than $1,000,000, or if a natural person, may be imprisoned for not more than 20 years, or both.\n#### 4. Determination required\nNot later than 90 days after the date of enactment of this Act, the Secretary of the Treasury shall submit a report to the Committee on Financial Services of the House of Representatives and the Committee on Banking, Housing, and Urban Affairs of the Senate determining whether the following are foreign persons described under section 3(a)(4):\n**(1)**\nGazprom.\n**(2)**\nRosneft.\n**(3)**\nLukoil.\n#### 5. Waiver\nWith respect to a foreign financial institution, the President may waive the requirements of section 3(a) for not more than 180 days at a time upon reporting to Congress that\u2014\n**(1)**\nthe waiver advances the objective of resolving the national emergency described in the Executive Order listed under section 3(a)(1); or\n**(2)**\nthe waiver is important to the national interest of the United States, provided that the President includes a detailed explanation of the reasons therefor.\n#### 6. Transfer of certain Russian assets held by United States financial institutions\n##### (a) Transfer from United States financial institutions\n**(1) In general**\nNot later than 90 days following the date of the enactment of this Act, the Secretary of the Treasury shall\u2014\n**(A)**\nseize, confiscate, transfer, or vest any covered Russian resources, in whole or in part, and including any interest or interests in such assets, held by a United States financial institution; and\n**(B)**\ndeposit the resulting funds into the Ukraine Support Fund established under subsection 104(d) of the REPO for Ukrainians Act ( 22 U.S.C. 9521 note), which may be used for the purposes specified in section 104(f) of such Act or for the purchase of defense articles for the Government of Ukraine.\n**(2) Authorities**\nThe Secretary of the Treasury shall have the same authority under this subsection with respect to covered Russian resources as are provided to the President under section 104(b) of the REPO for Ukrainians Act ( 22 U.S.C. 9521 note) with respect to Russian aggressor state sovereign assets.\n##### (b) Waiver\nThe President may waive the requirements of subsection (a) for up to 180 days at a time, for a cumulative period not to exceed 1 year, upon reporting to Congress in writing that\u2014\n**(1)**\nthe Government of the Russian Federation is taking meaningful steps to cease its destabilizing activities with respect to the sovereignty and territorial integrity of Ukraine; or\n**(2)**\nthe waiver is important to the national interest of the United States.\n##### (c) Definitions\nIn this section:\n**(1) Covered Russian resources**\nThe term covered Russian resources means funds and other property of the Central Bank of the Russian Federation, the Russian National Wealth Fund, or the Ministry of Finance of the Russian Federation that\u2014\n**(A)**\nare included in a report pursuant to\u2014\n**(i)**\ndirective 4 of Executive Order 14024; or\n**(ii)**\nsection 104(a) of the REPO for Ukrainians Act ( 22 U.S.C. 9521 note); and\n**(B)**\nare located in the United States.\n**(2) United States financial institution**\nThe term United States financial institution means\u2014\n**(A)**\na financial institution specified in subparagraph (A), (B), (C), (D), (E), (F), (G), (H), (I), (J), (M), or (AA) section 5312(a)(2) of title 31, United States Code, as amended by the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021; and\n**(B)**\nsuch other persons or entities as the Secretary of the Treasury determines appropriate.\n#### 7. Termination\nThis Act shall have no force or effect on the earlier of\u2014\n**(1)**\n30 days after the date that the President reports to Congress that the Russian Federation has ceased destabilizing activities with respect to the sovereignty and territorial integrity of Ukraine; or\n**(2)**\nthe date that is 5 years after the date of the enactment of this Act.",
      "versionDate": "2025-10-03",
      "versionType": "Reported in House"
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
        "actionDate": "2025-07-07",
        "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4301",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "PEACE Act of 2025",
      "type": "HR"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-08-20T17:05:39Z"
          },
          {
            "name": "Bank accounts, deposits, capital",
            "updateDate": "2025-08-20T17:05:00Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-08-20T17:05:28Z"
          },
          {
            "name": "Conflicts and wars",
            "updateDate": "2025-08-20T17:02:39Z"
          },
          {
            "name": "Department of the Treasury",
            "updateDate": "2025-08-20T17:05:52Z"
          },
          {
            "name": "Europe",
            "updateDate": "2025-08-20T17:04:53Z"
          },
          {
            "name": "Foreign and international banking",
            "updateDate": "2025-08-20T17:05:07Z"
          },
          {
            "name": "Fraud offenses and financial crimes",
            "updateDate": "2025-08-20T17:06:00Z"
          },
          {
            "name": "Presidents and presidential powers, Vice Presidents",
            "updateDate": "2025-08-20T17:05:21Z"
          },
          {
            "name": "Russia",
            "updateDate": "2025-08-20T17:02:46Z"
          },
          {
            "name": "Sanctions",
            "updateDate": "2025-08-20T17:05:13Z"
          },
          {
            "name": "Ukraine",
            "updateDate": "2025-08-20T17:04:48Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-07-29T22:09:02Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4346ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2025-10-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4346rh.xml"
        }
      ],
      "type": "Reported in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "PEACE Act of 2025",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2025-10-04T05:23:15Z"
    },
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "Preventing the Escalation of Armed Conflict in Europe Act of 2025",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2025-10-04T05:23:15Z"
    },
    {
      "title": "PEACE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:12:48Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PEACE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-19T07:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Preventing the Escalation of Armed Conflict in Europe Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-19T07:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To secure a peaceful resolution to the Russia-Ukraine conflict by requiring the Secretary of the Treasury to prohibit, or impose strict conditions on, the opening or maintaining in the United States of a correspondent account or a payable-through account by certain foreign financial institutions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-19T07:03:30Z"
    }
  ]
}
```
