# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/385?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/385
- Title: Combating Global Corruption Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 385
- Origin chamber: House
- Introduced date: 2025-01-14
- Update date: 2026-04-23T08:07:15Z
- Update date including text: 2026-04-23T08:07:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-14: Introduced in House
- 2025-01-14 - IntroReferral: Introduced in House
- 2025-01-14 - IntroReferral: Introduced in House
- 2025-01-14 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-14 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-01-14: Introduced in House

## Actions

- 2025-01-14 - IntroReferral: Introduced in House
- 2025-01-14 - IntroReferral: Introduced in House
- 2025-01-14 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-14 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-14",
    "latestAction": {
      "actionDate": "2025-01-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/385",
    "number": "385",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "C001068",
        "district": "9",
        "firstName": "Steve",
        "fullName": "Rep. Cohen, Steve [D-TN-9]",
        "lastName": "Cohen",
        "party": "D",
        "state": "TN"
      }
    ],
    "title": "Combating Global Corruption Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-23T08:07:15Z",
    "updateDateIncludingText": "2026-04-23T08:07:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-14",
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
      "actionDate": "2025-01-14",
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
      "actionDate": "2025-01-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-14",
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
          "date": "2025-01-14T15:00:45Z",
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
          "date": "2025-01-14T15:00:40Z",
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
      "bioguideId": "K000375",
      "district": "9",
      "firstName": "William",
      "fullName": "Rep. Keating, William R. [D-MA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Keating",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-01-14",
      "state": "MA"
    },
    {
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "SC"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "FL"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr385ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 385\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 14, 2025 Mr. Cohen (for himself, Mr. Keating , Mr. Wilson of South Carolina , and Ms. Salazar ) introduced the following bill; which was referred to the Committee on Foreign Affairs , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo identify and combat corruption in countries, to establish a tiered list of countries with respect to levels of corruption by their governments and their efforts to combat such corruption, and to evaluate whether foreign persons engaged in significant corruption should be specially designated nationals under the Global Magnitsky Human Rights Accountability Act.\n#### 1. Short title\nThis Act may be cited as the Combating Global Corruption Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Corrupt actor**\nThe term corrupt actor means\u2014\n**(A)**\nany foreign person or entity that is a government official or government entity responsible for, or complicit in, an act of corruption; and\n**(B)**\nany company, in which a person or entity described in subparagraph (A) has a significant stake, which is responsible for, or complicit in, an act of corruption.\n**(2) Corruption**\nThe term corruption means the unlawful exercise of entrusted public power for private gain, including by bribery, nepotism, fraud, or embezzlement.\n**(3) Significant corruption**\nThe term significant corruption means corruption committed at a high level of government that\u2014\n**(A)**\nillegitimately distorts major decision-making, such as policy or resource determinations, or other fundamental functions of governance; and\n**(B)**\ninvolves economically or socially large-scale government activities.\n#### 3. Publication of tiered ranking list\n##### (a) In general\nThe Secretary of State shall annually publish, on a publicly accessible website, a tiered ranking of all foreign countries.\n##### (b) Tier 1 countries\nA country shall be ranked as a tier 1 country in the ranking published under subsection (a) if the government of such country is complying with the minimum standards set forth in section 4.\n##### (c) Tier 2 countries\nA country shall be ranked as a tier 2 country in the ranking published under subsection (a) if the government of such country is making efforts to comply with the minimum standards set forth in section 4, but is not achieving the requisite level of compliance to be ranked as a tier 1 country.\n##### (d) Tier 3 countries\nA country shall be ranked as a tier 3 country in the ranking published under subsection (a) if the government of such country is making de minimis or no efforts to comply with the minimum standards set forth in section 4.\n#### 4. Minimum standards for the elimination of corruption and assessment of efforts to combat corruption\n##### (a) In general\nThe government of a country is complying with the minimum standards for the elimination of corruption if the government\u2014\n**(1)**\nhas enacted and implemented laws and established government structures, policies, and practices that prohibit and generally deter corruption, including significant corruption;\n**(2)**\nenforces the laws described in paragraph (1) by punishing any person who is found, through a fair judicial process, to have violated such laws;\n**(3)**\nprescribes punishment for significant corruption that is commensurate with the punishment prescribed for serious crimes; and\n**(4)**\nis making serious and sustained efforts to address corruption, including through prevention.\n##### (b) Factors for assessing government efforts To combat corruption\nIn determining whether a government is making serious and sustained efforts to address corruption, the Secretary of State shall consider, to the extent relevant or appropriate, factors such as\u2014\n**(1)**\nwhether the government of the country has criminalized corruption, investigates and prosecutes acts of corruption, and convicts and sentences persons responsible for such acts over which it has jurisdiction, including, as appropriate, incarcerating individuals convicted of such acts;\n**(2)**\nwhether the government of the country vigorously investigates, prosecutes, convicts, and sentences public officials who participate in or facilitate corruption, including nationals of the country who are deployed in foreign military assignments, trade delegations abroad, or other similar missions, who engage in or facilitate significant corruption;\n**(3)**\nwhether the government of the country has adopted measures to prevent corruption, such as measures to inform and educate the public, including potential victims, about the causes and consequences of corruption;\n**(4)**\nwhether the government of the country has taken steps to prohibit government officials from participating in, facilitating, or condoning corruption, including the investigation, prosecution, and conviction of such officials;\n**(5)**\nthe extent to which the country provides access, or, as appropriate, makes adequate resources available, to civil society organizations and other institutions to combat corruption, including reporting, investigating, and monitoring;\n**(6)**\nwhether an independent judiciary or judicial body in the country is responsible for, and effectively capable of, deciding corruption cases impartially, on the basis of facts and in accordance with the law, without any improper restrictions, influences, inducements, pressures, threats, or interferences (direct or indirect);\n**(7)**\nwhether the government of the country is assisting in international investigations of transnational corruption networks and in other cooperative efforts to combat significant corruption, including, as appropriate, cooperating with the governments of other countries to extradite corrupt actors;\n**(8)**\nwhether the government of the country recognizes the rights of victims of corruption, ensures their access to justice, and takes steps to prevent victims from being further victimized or persecuted by corrupt actors, government officials, or others;\n**(9)**\nwhether the government of the country protects victims of corruption or whistleblowers from reprisal due to such persons having assisted in exposing corruption, and refrains from other discriminatory treatment of such persons;\n**(10)**\nwhether the government of the country is willing and able to recover and, as appropriate, return the proceeds of corruption;\n**(11)**\nwhether the government of the country is taking steps to implement financial transparency measures in line with the Financial Action Task Force recommendations, including due diligence and beneficial ownership transparency requirements;\n**(12)**\nwhether the government of the country is facilitating corruption in other countries in connection with state-directed investment, loans or grants for major infrastructure, or other initiatives; and\n**(13)**\nsuch other information relating to corruption as the Secretary of State considers appropriate.\n##### (c) Assessing government efforts To combat corruption in relation to relevant international commitments\nIn determining whether a government is making serious and sustained efforts to address corruption, the Secretary of State shall consider the government of a country\u2019s compliance with the following, as relevant:\n**(1)**\nThe Inter-American Convention against Corruption of the Organization of American States, done at Caracas March 29, 1996.\n**(2)**\nThe Convention on Combating Bribery of Foreign Public Officials in International Business Transactions of the Organisation of Economic Co-operation and Development, done at Paris December 21, 1997 (commonly referred to as the Anti-Bribery Convention ).\n**(3)**\nThe United Nations Convention against Transnational Organized Crime, done at New York November 15, 2000.\n**(4)**\nThe United Nations Convention against Corruption, done at New York October 31, 2003.\n**(5)**\nSuch other treaties, agreements, and international standards as the Secretary of State considers appropriate.\n#### 5. Imposition of sanctions under Global Magnitsky Human Rights Accountability Act\n##### (a) In general\nThe Secretary of State, in coordination with the Secretary of the Treasury, should evaluate whether there are foreign persons engaged in significant corruption for the purposes of potential imposition of sanctions under the Global Magnitsky Human Rights Accountability Act (subtitle F of title XII of Public Law 114\u2013328 ; 22 U.S.C. 2656 note) in all countries identified as tier 3 countries under section 3.\n##### (b) Report required\nNot later than 180 days after publishing the list required by section 3(a) and annually thereafter, the Secretary of State shall submit to the committees specified in subsection (e) a report that includes\u2014\n**(1)**\na list of foreign persons with respect to which the President imposed sanctions pursuant to the evaluation under subsection (a);\n**(2)**\nthe dates on which such sanctions were imposed; and\n**(3)**\nthe reasons for imposing such sanctions.\n##### (c) Form of report\nEach report required by subsection (b) shall be submitted in unclassified form but may include a classified annex.\n##### (d) Briefing in lieu of report\nThe Secretary of State, in coordination with the Secretary of the Treasury, may provide a briefing to the committees specified in subsection (e) instead of submitting a written report required under subsection (b), if doing so would better serve existing United States anti-corruption efforts or the national interests of the United States.\n##### (e) Committees specified\nThe committees specified in this subsection are\u2014\n**(1)**\nthe Committee on Foreign Relations, the Committee on Appropriations, the Committee on Banking, Housing, and Urban Affairs, and the Committee on the Judiciary of the Senate; and\n**(2)**\nthe Committee on Foreign Affairs, the Committee on Appropriations, the Committee on Financial Services, and the Committee on the Judiciary of the House of Representatives.\n#### 6. Designation of embassy anti-corruption points of contact\n##### (a) In general\nThe Secretary of State shall annually designate an anti-corruption point of contact at the United States diplomatic post to each country identified as tier 2 or tier 3 under section 3, or which the Secretary otherwise determines is in need of such a point of contact. The point of contact shall be the chief of mission or the chief of mission's designee.\n##### (b) Responsibilities\nEach anti-corruption point of contact designated under subsection (a) shall be responsible for enhancing coordination and promoting the implementation of a whole-of-government approach among the relevant Federal departments and agencies undertaking efforts to\u2014\n**(1)**\npromote good governance in foreign countries; and\n**(2)**\nenhance the ability of such countries\u2014\n**(A)**\nto combat public corruption; and\n**(B)**\nto develop and implement corruption risk assessment tools and mitigation strategies.\n##### (c) Training\nThe Secretary of State shall implement appropriate training for anti-corruption points of contact designated under subsection (a).",
      "versionDate": "2025-01-14",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional oversight",
            "updateDate": "2025-04-25T17:52:53Z"
          },
          {
            "name": "Crime prevention",
            "updateDate": "2025-04-25T17:52:53Z"
          },
          {
            "name": "Crime victims",
            "updateDate": "2025-04-25T17:52:53Z"
          },
          {
            "name": "Criminal investigation, prosecution, interrogation",
            "updateDate": "2025-04-25T17:52:53Z"
          },
          {
            "name": "Criminal procedure and sentencing",
            "updateDate": "2025-04-25T17:52:53Z"
          },
          {
            "name": "Diplomacy, foreign officials, Americans abroad",
            "updateDate": "2025-04-25T17:52:53Z"
          },
          {
            "name": "Employment discrimination and employee rights",
            "updateDate": "2025-04-25T17:52:53Z"
          },
          {
            "name": "Energy storage, supplies, demand",
            "updateDate": "2025-04-25T17:52:53Z"
          },
          {
            "name": "Europe",
            "updateDate": "2025-04-25T17:52:53Z"
          },
          {
            "name": "Foreign aid and international relief",
            "updateDate": "2025-04-25T17:52:53Z"
          },
          {
            "name": "Germany",
            "updateDate": "2025-04-25T17:52:53Z"
          },
          {
            "name": "Government ethics and transparency, public corruption",
            "updateDate": "2025-04-25T17:52:53Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-04-25T17:52:53Z"
          },
          {
            "name": "Human rights",
            "updateDate": "2025-04-25T17:52:53Z"
          },
          {
            "name": "International law and treaties",
            "updateDate": "2025-04-25T17:52:53Z"
          },
          {
            "name": "International organizations and cooperation",
            "updateDate": "2025-04-25T17:52:53Z"
          },
          {
            "name": "Judicial procedure and administration",
            "updateDate": "2025-04-25T17:52:53Z"
          },
          {
            "name": "Oil and gas",
            "updateDate": "2025-04-25T17:52:53Z"
          },
          {
            "name": "Organized crime",
            "updateDate": "2025-04-25T17:52:53Z"
          },
          {
            "name": "Pipelines",
            "updateDate": "2025-04-25T17:52:53Z"
          },
          {
            "name": "Russia",
            "updateDate": "2025-04-25T17:52:53Z"
          },
          {
            "name": "Sanctions",
            "updateDate": "2025-04-25T17:52:53Z"
          },
          {
            "name": "Sovereignty, recognition, national governance and status",
            "updateDate": "2025-04-25T17:52:53Z"
          },
          {
            "name": "U.S. and foreign investments",
            "updateDate": "2025-04-25T17:52:53Z"
          },
          {
            "name": "United Nations",
            "updateDate": "2025-04-25T17:52:53Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-02-21T12:16:32Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-14",
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
          "measure-id": "id119hr385",
          "measure-number": "385",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-14",
          "originChamber": "HOUSE",
          "update-date": "2025-02-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr385v00",
            "update-date": "2025-02-28"
          },
          "action-date": "2025-01-14",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Combating Global Corruption Act of 2025 </strong></p><p>This bill requires the Department of State to address corruption in foreign governments.</p><p>The State Department must annually publish a ranking of foreign countries based on their government's efforts to eliminate corruption. Corruption, for the purposes of the bill, is the unlawful exercise of entrusted public power for private gain, including by bribery, nepotism, fraud, or embezzlement.</p><p>The bill outlines the minimum standards that the State Department must consider when creating the ranking. These considerations include, for example, whether a country has criminalized corruption, adopted measures to prevent corruption, and complied with the United Nations Convention against Corruption and other relevant international agreements. Tier one countries meet the standards; tier two countries make some efforts to meet the standards; tier three countries make <em>de minimis</em> or no efforts to meet the standards.</p><p>If a country is ranked in the second or third tier, the State Department must designate an anti-corruption contact at the U.S. diplomatic post in that country to promote good governance and combat corruption.</p><p>The State Department must also evaluate whether there are foreign persons (individuals or entities) engaged in significant corruption in all third-tier countries for the purpose of potential imposition of sanctions under the Global Magnitsky Human Rights Accountability Act. The State Department must annually provide Congress with a list of those persons that the President has sanctioned pursuant to this evaluation, the dates sanctions were imposed, and the reasons for imposing sanctions.</p>"
        },
        "title": "Combating Global Corruption Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr385.xml",
    "summary": {
      "actionDate": "2025-01-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Combating Global Corruption Act of 2025 </strong></p><p>This bill requires the Department of State to address corruption in foreign governments.</p><p>The State Department must annually publish a ranking of foreign countries based on their government's efforts to eliminate corruption. Corruption, for the purposes of the bill, is the unlawful exercise of entrusted public power for private gain, including by bribery, nepotism, fraud, or embezzlement.</p><p>The bill outlines the minimum standards that the State Department must consider when creating the ranking. These considerations include, for example, whether a country has criminalized corruption, adopted measures to prevent corruption, and complied with the United Nations Convention against Corruption and other relevant international agreements. Tier one countries meet the standards; tier two countries make some efforts to meet the standards; tier three countries make <em>de minimis</em> or no efforts to meet the standards.</p><p>If a country is ranked in the second or third tier, the State Department must designate an anti-corruption contact at the U.S. diplomatic post in that country to promote good governance and combat corruption.</p><p>The State Department must also evaluate whether there are foreign persons (individuals or entities) engaged in significant corruption in all third-tier countries for the purpose of potential imposition of sanctions under the Global Magnitsky Human Rights Accountability Act. The State Department must annually provide Congress with a list of those persons that the President has sanctioned pursuant to this evaluation, the dates sanctions were imposed, and the reasons for imposing sanctions.</p>",
      "updateDate": "2025-02-28",
      "versionCode": "id119hr385"
    },
    "title": "Combating Global Corruption Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Combating Global Corruption Act of 2025 </strong></p><p>This bill requires the Department of State to address corruption in foreign governments.</p><p>The State Department must annually publish a ranking of foreign countries based on their government's efforts to eliminate corruption. Corruption, for the purposes of the bill, is the unlawful exercise of entrusted public power for private gain, including by bribery, nepotism, fraud, or embezzlement.</p><p>The bill outlines the minimum standards that the State Department must consider when creating the ranking. These considerations include, for example, whether a country has criminalized corruption, adopted measures to prevent corruption, and complied with the United Nations Convention against Corruption and other relevant international agreements. Tier one countries meet the standards; tier two countries make some efforts to meet the standards; tier three countries make <em>de minimis</em> or no efforts to meet the standards.</p><p>If a country is ranked in the second or third tier, the State Department must designate an anti-corruption contact at the U.S. diplomatic post in that country to promote good governance and combat corruption.</p><p>The State Department must also evaluate whether there are foreign persons (individuals or entities) engaged in significant corruption in all third-tier countries for the purpose of potential imposition of sanctions under the Global Magnitsky Human Rights Accountability Act. The State Department must annually provide Congress with a list of those persons that the President has sanctioned pursuant to this evaluation, the dates sanctions were imposed, and the reasons for imposing sanctions.</p>",
      "updateDate": "2025-02-28",
      "versionCode": "id119hr385"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr385ih.xml"
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
      "title": "Combating Global Corruption Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-08T05:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Combating Global Corruption Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-08T05:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To identify and combat corruption in countries, to establish a tiered list of countries with respect to levels of corruption by their governments and their efforts to combat such corruption, and to evaluate whether foreign persons engaged in significant corruption should be specially designated nationals under the Global Magnitsky Human Rights Accountability Act.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-08T05:48:23Z"
    }
  ]
}
```
