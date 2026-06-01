# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/589?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/589
- Title: SAD Act
- Congress: 119
- Bill type: S
- Bill number: 589
- Origin chamber: Senate
- Introduced date: 2025-02-13
- Update date: 2025-12-05T21:54:19Z
- Update date including text: 2025-12-05T21:54:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-13: Introduced in Senate
- 2025-02-13 - IntroReferral: Introduced in Senate
- 2025-02-13 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-02-13: Introduced in Senate

## Actions

- 2025-02-13 - IntroReferral: Introduced in Senate
- 2025-02-13 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/589",
    "number": "589",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "W000817",
        "district": "",
        "firstName": "Elizabeth",
        "fullName": "Sen. Warren, Elizabeth [D-MA]",
        "lastName": "Warren",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "SAD Act",
    "type": "S",
    "updateDate": "2025-12-05T21:54:19Z",
    "updateDateIncludingText": "2025-12-05T21:54:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-13",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-02-13T19:57:11Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "OR"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "WA"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernard",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-02-13",
      "state": "VT"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "VT"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "OR"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "CT"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "HI"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "NJ"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "MA"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "NV"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "IL"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s589is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 589\nIN THE SENATE OF THE UNITED STATES\nFebruary 13, 2025 Ms. Warren (for herself, Mr. Merkley , Mrs. Murray , Mr. Sanders , Mr. Welch , Mr. Wyden , Mr. Blumenthal , Ms. Hirono , Mr. Booker , Mr. Markey , Ms. Cortez Masto , and Mr. Durbin ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo prohibit disinformation in the advertising of abortion services, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Antiabortion Disinformation Act or the SAD Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nAbortion services are an essential component of reproductive health care.\n**(2)**\nAfter decades of escalating attacks on abortion rights, on June 24, 2022, in Dobbs v. Jackson Women\u2019s Health Organization, the Supreme Court overruled Roe v. Wade, reversing decades of precedent recognizing a constitutional right to abortion and permitting decimation of an already precarious landscape of access to abortion.\n**(3)**\nThe effects were immediate and disastrous. As of January 2025, abortion is unavailable in 14 States, leaving 17.9 million women, as well as transgender and gender nonconforming individuals, of reproductive age (ages 15 to 49), without access to abortion in the home State of such individuals.\n**(4)**\nTravel time to an abortion clinic, already burdensome under Roe, has quadrupled since Dobbs, as scores of clinics in already underserved areas have been forced to close and more patients have been forced to travel to other States (with over 170,000 people traveling out of State for care in 2023 alone). As distance to an abortion facility increases, so do the accompanying burdens of time off from work or school, lost wages, transportation costs, lodging, child care costs, and other ancillary costs.\n**(5)**\nThese burdens do not fall equally. Since Dobbs and additional State bans and restrictions on abortion care have taken effect, data shows that women with low incomes and women of color have experienced the largest increase in travel times to abortion clinics. This is particularly burdensome for women and pregnant people of color in the South, the area of the country that has seen the highest increases in travel time.\n**(6)**\nThe freedom to decide whether and when to have a child is key to the ability of an individual to participate fully in our democracy.\n**(7)**\nUnfortunately, rampant misinformation and disinformation have affected the ability of people to access needed abortion care. Crisis pregnancy centers (CPCs) often disseminate and promote inaccurate information about abortion and contraception.\n**(8)**\nCPCs are antiabortion organizations that present themselves as comprehensive reproductive health care providers with the intent of shaming, deceiving, or discouraging pregnant people from having abortions.\n**(9)**\nAccording to the Journal of Medical Internet Research (JMIR) Public Health and Surveillance, there are more than 2,500 CPCs in the United States, though some antiabortion groups claim that the number is closer to 4,000.\n**(10)**\nAccording to 2020 data from JMIR Public Health and Surveillance, CPCs outnumber abortion clinics nationwide by an average of 3 to 1. In some States, this statistic is higher. For example, The Alliance: State Advocates for Women\u2019s Rights & Gender Equality (The Alliance) found that in Pennsylvania, CPCs outnumber abortion clinics by 9 to 1. The Alliance also found that in Minnesota, CPCs outnumber abortion clinics by 11 to 1.\n**(11)**\nCPCs routinely engage in a variety of deceptive tactics, including\u2014\n**(A)**\nmaking false claims about reproductive health care and providers;\n**(B)**\ndisseminating inaccurate, misleading, and stigmatizing information about the risks of abortion and contraception; and\n**(C)**\nusing illegitimate or false citations to imply that deceptive claims are supported by legitimate medical sources.\n**(12)**\nCPCs typically advertise themselves as providers of comprehensive health care. However, most CPCs in the United States do not employ licensed medical personnel or provide referrals for birth control or abortion care.\n**(13)**\nMost CPCs are not Health Insurance Portability and Accountability Act (HIPAA)-covered entities, but many deceptively claim to be compliant with HIPAA in order to collect sensitive information and mislead pregnant people about the privacy practices and obligations of CPCs. CPCs have been found to disclose the health data of pregnant people, including to law enforcement.\n**(14)**\nBy using these deceptive tactics, CPCs prevent people from accessing reproductive health care, intentionally delay access to time-sensitive abortion services, and can subject people to harmful interactions with law enforcement. The consequences of these tactics and delays are far greater in the wake of Dobbs.\n**(15)**\nCPCs target under-resourced neighborhoods and communities of color, including Black, Latino, Indigenous, Asian-American, Pacific Islander, and immigrant communities, by locating CPCs near social services centers and comprehensive reproductive health care providers. CPCs place advertisements in these neighborhoods that mislead and draw people away from nearby providers that offer evidence-based sexual and reproductive health care, including abortion care. This exacerbates existing health barriers and delays access to time-sensitive care.\n**(16)**\nPeople are entitled to honest, accurate, and timely information when seeking reproductive health care.\n#### 3. Prohibition on disinformation relating to abortion services\n##### (a) Prohibition\nIt shall be unlawful for any person to engage in deceptive advertising about the reproductive health services offered by the person, including advertising that misrepresents that the person\u2014\n**(1)**\noffers or provides contraception or abortion services (or referrals for such contraception or abortion services); or\n**(2)**\nemploys or offers access to licensed medical personnel.\n##### (b) Rulemaking\nThe Commission may promulgate, under section 553 of title 5, United States Code, any regulations the Commission determines necessary to carry out this section.\n##### (c) Enforcement by Commission\n**(1) Unfair or deceptive acts or practices**\nA violation of this section or a regulation promulgated pursuant to this section shall be treated as a violation of a regulation under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ) regarding unfair or deceptive acts or practices.\n**(2) Powers of Commission**\nExcept as otherwise provided in paragraph (3), the Commission shall enforce this section and any regulation promulgated pursuant to this section in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act were incorporated into and made a part of this section, and any person who violates this section or a regulation promulgated pursuant to this section shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act.\n**(3) Nonprofit organizations**\nNotwithstanding section 4, 5(a)(2), or 6 of the Federal Trade Commission Act ( 15 U.S.C. 44 ; 45(a)(2); 46) or any jurisdictional limitation of the Commission, the Commission shall also enforce this section and any regulation promulgated pursuant to this section in the same manner provided in paragraphs (1) and (2) with respect to organizations not organized to carry on business for their own profit or that of their members.\n**(4) Independent litigation authority**\n**(A) Civil action by Commission**\nIf the Commission has reason to believe that a person has violated this section or a regulation promulgated pursuant to this section, the Commission may bring a civil action in any appropriate United States district court for any of the following remedies:\n**(i)**\nTo enjoin any further such violation by such person.\n**(ii)**\nTo enforce compliance with this section or a regulation promulgated pursuant to this section.\n**(iii)**\nTo obtain a permanent, temporary, or preliminary injunction.\n**(iv)**\nTo obtain civil penalties.\n**(v)**\nTo obtain damages, restitution, or other compensation on behalf of aggrieved consumers.\n**(vi)**\nTo obtain any other appropriate equitable relief.\n**(B) Exclusive authority of Commission**\n**(i) Exclusive authority**\nExcept as otherwise provided in section 16(a)(3) of the Federal Trade Commission Act ( 15 U.S.C. 56(a)(3) ), the Commission shall have exclusive authority to commence or defend, and supervise the litigation of, any civil action under this section and any appeal of such action, in its own name by any of its attorneys, designated by it for such purpose, unless the Commission authorizes the Attorney General to do so.\n**(ii) Relation to Attorney General**\nThe Commission shall inform the Attorney General of the exercise of such authority, and such exercise shall not preclude the Attorney General from intervening on behalf of the United States in such action and any appeal of such action as may be otherwise provided by law.\n##### (d) Civil penalty\nIn addition to any other penalty as may be prescribed by law, any person who violates this section or a regulation promulgated pursuant this section shall be punishable by a civil penalty for each such violation that shall not exceed the greater of\u2014\n**(1)**\n$100,000 (to be adjusted annually for inflation based on the change in the Consumer Price Index); or\n**(2)**\n50 percent of the revenue earned by the ultimate parent entity of a person during the preceding 12-month period.\n##### (e) Reports\nBeginning 1 year after the date of the enactment of this Act, and every 2 years thereafter, the Commission shall submit to Congress a report that includes (with respect to the previous year) a description of\u2014\n**(1)**\nany enforcement action by the Commission under this Act;\n**(2)**\nthe outcome of any such action; and\n**(3)**\nany regulation promulgated pursuant to this Act.\n##### (f) Savings clause\nNothing in this Act may be construed to limit the authority of the Commission under any other provision of law.\n##### (g) Definitions\nIn this Act:\n**(1) Abortion services**\nThe term abortion services means an abortion or any medical or non-medical service related to or provided in conjunction with an abortion, whether or not provided at the same time or on the same day as the abortion.\n**(2) Commission**\nThe term Commission means the Federal Trade Commission.\n**(3) Person**\nThe term person has the meaning given that term in section 551(2) of title 5, United States Code.",
      "versionDate": "2025-02-13",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-01-31",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "846",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "SAD Act",
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
            "name": "Abortion",
            "updateDate": "2025-06-09T15:40:05Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-06-09T15:40:05Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-06-09T15:40:05Z"
          },
          {
            "name": "Family planning and birth control",
            "updateDate": "2025-06-09T15:40:05Z"
          },
          {
            "name": "Federal Trade Commission (FTC)",
            "updateDate": "2025-06-09T15:40:05Z"
          },
          {
            "name": "Marketing and advertising",
            "updateDate": "2025-06-09T15:40:05Z"
          },
          {
            "name": "Sex and reproductive health",
            "updateDate": "2025-06-09T15:40:05Z"
          },
          {
            "name": "Women's health",
            "updateDate": "2025-06-09T15:40:05Z"
          }
        ]
      },
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-05-13T20:19:05Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-13",
    "originChamber": "Senate",
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
          "measure-id": "id119s589",
          "measure-number": "589",
          "measure-type": "s",
          "orig-publish-date": "2025-02-13",
          "originChamber": "SENATE",
          "update-date": "2025-09-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s589v00",
            "update-date": "2025-09-09"
          },
          "action-date": "2025-02-13",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Stop Antiabortion Disinformation Act or the SAD Act </strong></p><p>This bill prohibits deceptive advertising for reproductive health services.</p><p>Specifically, the bill makes it unlawful for a person (i.e., individual, partnership, corporation, association, or organization) to deceptively advertise the reproductive health services they offer, including by misrepresenting that the person (1) offers or provides contraception or abortion services (or referrals for such contraception or abortion services), or (2) employs or offers access to licensed medical personnel.</p><p>The bill provides for enforcement by the Federal Trade Commission.</p><p>In addition to any other penalty, violations are subject to a civil penalty that may not exceed the greater of $100,000 (adjusted annually for inflation)\u00a0or 50%\u00a0of the revenue earned during the preceding 12-month period by the ultimate parent entity of the person who violated the bill.\u00a0</p>"
        },
        "title": "SAD Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s589.xml",
    "summary": {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Stop Antiabortion Disinformation Act or the SAD Act </strong></p><p>This bill prohibits deceptive advertising for reproductive health services.</p><p>Specifically, the bill makes it unlawful for a person (i.e., individual, partnership, corporation, association, or organization) to deceptively advertise the reproductive health services they offer, including by misrepresenting that the person (1) offers or provides contraception or abortion services (or referrals for such contraception or abortion services), or (2) employs or offers access to licensed medical personnel.</p><p>The bill provides for enforcement by the Federal Trade Commission.</p><p>In addition to any other penalty, violations are subject to a civil penalty that may not exceed the greater of $100,000 (adjusted annually for inflation)\u00a0or 50%\u00a0of the revenue earned during the preceding 12-month period by the ultimate parent entity of the person who violated the bill.\u00a0</p>",
      "updateDate": "2025-09-09",
      "versionCode": "id119s589"
    },
    "title": "SAD Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Stop Antiabortion Disinformation Act or the SAD Act </strong></p><p>This bill prohibits deceptive advertising for reproductive health services.</p><p>Specifically, the bill makes it unlawful for a person (i.e., individual, partnership, corporation, association, or organization) to deceptively advertise the reproductive health services they offer, including by misrepresenting that the person (1) offers or provides contraception or abortion services (or referrals for such contraception or abortion services), or (2) employs or offers access to licensed medical personnel.</p><p>The bill provides for enforcement by the Federal Trade Commission.</p><p>In addition to any other penalty, violations are subject to a civil penalty that may not exceed the greater of $100,000 (adjusted annually for inflation)\u00a0or 50%\u00a0of the revenue earned during the preceding 12-month period by the ultimate parent entity of the person who violated the bill.\u00a0</p>",
      "updateDate": "2025-09-09",
      "versionCode": "id119s589"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s589is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "SAD Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-24T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SAD Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stop Antiabortion Disinformation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit disinformation in the advertising of abortion services, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:19:17Z"
    }
  ]
}
```
