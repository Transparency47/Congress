# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3892?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3892
- Title: Stop Price Gouging in Grocery Stores Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3892
- Origin chamber: Senate
- Introduced date: 2026-02-12
- Update date: 2026-05-20T11:03:29Z
- Update date including text: 2026-05-20T11:03:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-12: Introduced in Senate
- 2026-02-12 - IntroReferral: Introduced in Senate
- 2026-02-12 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2026-02-12: Introduced in Senate

## Actions

- 2026-02-12 - IntroReferral: Introduced in Senate
- 2026-02-12 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-12",
    "latestAction": {
      "actionDate": "2026-02-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3892",
    "number": "3892",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "L000570",
        "district": "",
        "firstName": "Ben",
        "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
        "lastName": "Luj\u00e1n",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "Stop Price Gouging in Grocery Stores Act of 2026",
    "type": "S",
    "updateDate": "2026-05-20T11:03:29Z",
    "updateDateIncludingText": "2026-05-20T11:03:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-12",
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
      "actionDate": "2026-02-12",
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
          "date": "2026-02-12T21:27:29Z",
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
      "sponsorshipDate": "2026-02-12",
      "state": "OR"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "NV"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "NY"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "NM"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2026-03-17",
      "state": "VT"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "MA"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "GA"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "sponsorshipWithdrawnDate": "2026-05-12",
      "state": "CO"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3892is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3892\nIN THE SENATE OF THE UNITED STATES\nFebruary 12, 2026 Mr. Luj\u00e1n (for himself, Mr. Merkley , Ms. Rosen , Mrs. Gillibrand , and Mr. Heinrich ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo prohibit retail food stores from price gouging and engaging in surveillance-based price setting practices, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Price Gouging in Grocery Stores Act of 2026 .\n#### 2. Prohibition on price gouging\n##### (a) Prohibition\nAn operator of a retail food store may not sell or offer for sale an item at a grossly excessive price.\n##### (b) Affirmative defense\nAn operator of a retail food store does not sell or offer for sale an item at a grossly excessive price in violation of subsection (a) if the retail food store demonstrates to the Commission that the increase in the price of the item involved is directly attributable to additional costs that are\u2014\n**(1)**\nnot within the control of the retail food store; and\n**(2)**\nincurred by the retail food store in procuring, acquiring, distributing, or providing the item.\n##### (c) Required guidance\nNot later than 180 days after the date of the enactment of this Act, the Commission shall promulgate, pursuant to section 553 of title 5, United States Code, regulations with respect to violations of subsection (a) that shall include guidelines on what constitutes (for purposes of this Act)\u2014\n**(1)**\na market;\n**(2)**\na grossly excessive price for an item; and\n**(3)**\nan excessive price for an item.\n##### (d) Definition of grossly excessive price\n**(1) In general**\nFor purposes of subsection (a) and the guidelines required by subsection (c), the Commission shall define the term grossly excessive price using any metric it deems appropriate.\n**(2) Definition considerations**\nIn formulating the definition described in paragraph (1), the Commission shall consider whether to provide that such term shall include a price for an item that is an amount equal to or greater than 120 percent (or a lesser percentage, as determined appropriate by the Commission) of the average price for such item in the market during the 6-month period preceding the sale or offer for sale that allegedly violates subsection (a).\n#### 3. Prohibition on surveillance-based price setting\n##### (a) Prohibition\nAn operator of a retail food store may not engage in surveillance-based price setting, including by\u2014\n**(1)**\nadjusting the price of any item for a consumer (directly or indirectly) based on the personal information of the consumer, including such personal information collected using facial recognition technology; or\n**(2)**\nusing an electronic shelf label to change the price of an item for a consumer based on the personal information of such consumer.\n##### (b) General exceptions\nAn operator of a retail food store does not engage in surveillance-based price setting in violation of subsection (a) if the retail food store demonstrates to the Commission that each of the following conditions are met:\n**(1)**\nA difference in the price of an item is based solely on reasonable costs associated with providing the item to different consumers.\n**(2)**\nA discounted price of an item is offered to members of a particular group that relates to occupation, age, military service, student status, or other factors approved by the Commission, based on publicly disclosed eligibility criteria.\n**(3)**\nAny discount or reward with respect to an item is offered uniformly to all consumers who meet the disclosed eligibility criteria.\n**(4)**\nAny personal information is used solely to offer or administer the discount or reward and is not used for any other purpose, including targeted advertising and surveillance-based price setting.\n##### (c) Exceptions for use of biometric data\nNotwithstanding subsection (a), an operator of a retail food store may use biometric data of an adult consumer if such consumer chooses to voluntarily verify the identity of such consumer by providing such biometric data, if such retail food store\u2014\n**(1)**\ninforms the consumer or the legally authorized representative of the consumer in writing that such biometric data is being collected, stored, or used by such retail food store;\n**(2)**\ninforms the consumer or the legally authorized representative of the consumer in writing of the specific purpose and length of term for which such biometric data is being collected, stored, and used;\n**(3)**\ninforms the consumer or the legally authorized representative of the consumer in writing of the specific circumstances under which biometric data is shared with law enforcement;\n**(4)**\nreceives a written release executed by the consumer or the legally authorized representative of the consumer for the collection, storage, or use of such biometric data; and\n**(5)**\ndoes not sell such biometric data to, or share such biometric data with, any third party.\n#### 4. Required disclosure of use of facial recognition technology\n##### (a) Requirement\nA retail food store that uses facial recognition technology at such retail food store shall notify consumers of such retail food store, in plain and simple language, about such use and the intended purpose of such technology and use through clear and conspicuous signage placed at the main entrance to the retail food store.\n##### (b) Limitation\nFor purposes of this section, the term retail food store does not include an online entity.\n#### 5. Prohibition on electronic shelf labels\n##### (a) Prohibition\nAn operator of a retail food store larger than 10,000 square feet\u2014\n**(1)**\nmay not use an electronic shelf label or any digital shelf display technology in such retail food store; and\n**(2)**\nshall use a non-digital presentation of the price of each item in such retail food store.\n##### (b) Rule of construction\nNothing in this section may be construed to prohibit a retail food store from providing a consumer, based on the purchase history of such consumer, a discounted or promotional price in accordance with the conditions described in section 3(b).\n##### (c) Limitation\nFor purposes of this section, the term retail food store does not include an online entity.\n#### 6. Enforcement\n##### (a) Enforcement by Federal Trade Commission\n**(1) Unfair or deceptive acts or practices**\nA violation of section 2(a), 3(a), 4(a), or 5(a) (or a regulation promulgated under such section) shall be treated as a violation of a rule defining an unfair or deceptive act or practice prescribed under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ) and as a violation of section 5(a) of such Act ( 15 U.S.C. 45(a) ) regarding unfair methods of competition.\n**(2) Powers of Commission**\nThe Commission shall enforce section 2(a), 3(a), 4(a), and 5(a) (and any regulations promulgated under such sections) in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this Act. Any retail food store that violates such sections (or any regulations promulgated under such sections) shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act.\n**(3) Authority preserved**\nNothing in this Act shall be construed to limit the authority of the Commission under any other provision of law.\n**(4) Regulations**\nThe Commission may promulgate, pursuant to section 553 of title 5, United States Code, any regulations the Commission determines necessary to carry out the provisions of this Act.\n##### (b) Actions by States\n**(1) In general**\nIn any case in which the attorney general of a State, or an official or agency of a State, has reason to believe that an interest of the residents of such State has been or is threatened or adversely affected by an act or practice in violation of section 2(a), 3(a), 4(a), or 5(a) (or a regulation promulgated under such section), the State, as parens patriae, may bring a civil action on behalf of the residents of the State in an appropriate State court or an appropriate district court of the United States to\u2014\n**(A)**\nenjoin such act or practice;\n**(B)**\nenforce compliance with such section (or such regulation);\n**(C)**\nobtain, for each such violation, the greater of\u2014\n**(i)**\nthe actual monetary damages incurred from the violation; or\n**(ii)**\n$3,000; or\n**(D)**\nobtain any restitution, penalties, and other legal or equitable relief as the court may deem just and proper.\n**(2) Rule of construction**\nNothing in this subsection may be construed to prevent an attorney general, official, or agency of a State from exercising the powers conferred on the attorney general, official, or agency by the laws of the State to conduct investigations, to administer oaths or affirmations, or to compel the attendance of witnesses or the production of documentary or other evidence.\n##### (c) Private right of action\n**(1) In general**\nA consumer injured by an act or practice in violation of section 2(a), 3(a), 4(a), or 5(a) (or a regulation promulgated under such section) may bring in an appropriate district court of the United States an action to\u2014\n**(A)**\nenjoin the violation;\n**(B)**\nsubject to paragraph (2), obtain, for each such violation, the greater of\u2014\n**(i)**\nthe actual monetary damages incurred from the violation; or\n**(ii)**\n$3,000; or\n**(C)**\nobtain any restitution, penalties, and other legal or equitable relief as the court may deem just and proper.\n**(2) Willful or knowing violations**\nIf the court finds that the defendant acted willfully or knowingly in committing a violation described in paragraph (1), the court shall increase the amount of the award to an amount that is 3 times the amount available under paragraph (1)(B).\n**(3) Costs and attorney\u2019s fees**\nThe court shall award to a prevailing plaintiff in an action under this subsection the costs of such action and reasonable attorney\u2019s fees, as determined by the court.\n**(4) Limitation**\nAn action may be commenced under this subsection not later than 5 years after the date on which a consumer first discovered or had a reasonable opportunity to discover the violation.\n**(5) Nonexclusive remedy**\nThe remedy provided by this subsection shall be in addition to any other remedies available to the consumer.\n**(6) Invalidity of pre-dispute arbitration and joint action waivers**\nNotwithstanding any other provision of law, a pre-dispute arbitration agreement or pre-dispute joint action waiver between a retail food store and a consumer shall not be valid or enforceable for purposes of this subsection.\n#### 7. Preemption of directly conflicting State laws\n##### (a) In general\nNothing in this Act may be construed to preempt, displace, or supplant any State law, except to the extent that a provision of State law conflicts with a provision of this Act, and then only to the extent of the conflict.\n##### (b) Greater protection under State law\nFor purposes of this section, a provision of State law does not conflict with a provision of this Act if such provision of State law provides additional protections to consumers protected under this Act with respect to price gouging, surveillance-based price setting, collecting personal information, or using facial recognition technology in retail food stores.\n#### 8. Authorization of appropriations\nThere is authorized to be appropriated for the fiscal year 2026 $5,000,000 (to remain available until September 30, 2032) to carry out this Act.\n#### 9. Definitions\nIn this Act:\n**(1) Biometric data**\nThe term biometric data means data generated by automatic measurements, including data gathered through the use of facial recognition technology, or other representations of the biological characteristics of a consumer, including\u2014\n**(A)**\nfingerprints;\n**(B)**\nvoice prints;\n**(C)**\niris or retina scans;\n**(D)**\ngait; and\n**(E)**\nother unique biological patterns.\n**(2) Commission**\nThe term Commission means the Federal Trade Commission.\n**(3) Electronic shelf label**\nThe term electronic shelf label means electronic and wireless paper (E-paper) displays or digital price tags that present product and pricing information.\n**(4) Electronic surveillance technology**\nThe term electronic surveillance technology means a technological method, system, or other tool of surveillance used to observe, monitor, or collect information related to an consumer, including sensors, cameras, device tracking, biometric monitoring, facial recognition technology, or other forms of observation or data collection that are capable of gathering personal information about a consumer.\n**(5) Facial recognition technology**\nThe term facial recognition technology means technology that facilitates or otherwise enables an automated or semi-automated process that\u2014\n**(A)**\nassists in identifying a consumer based on the physical characteristics of the face of such consumer; or\n**(B)**\nlogs characteristics of the face, head, or body of a consumer to infer the emotion, associations, activities, or location of such consumer.\n**(6) Item**\nThe term item means a specific and distinct product, good, or commodity available for sale.\n**(7) Non-digital presentation of price**\nThe term non-digital presentation of price means\u2014\n**(A)**\na sign that offers the unit price for 1 or more brands or sizes of a given item;\n**(B)**\na sticker, stamp, sign, label, or tag affixed to the shelf upon which the item is displayed; or\n**(C)**\na sticker, stamp, sign, label, or tag affixed to the item.\n**(8) Personal information**\nThe term personal information means any quality, feature, attribute, or trait of a consumer that is reasonably capable of being associated with, or could be reasonably linked to, directly or indirectly, a particular consumer or a household of a particular consumer, including\u2014\n**(A)**\nany immutable characteristic, including race, ethnicity, and eye color;\n**(B)**\nany mutable characteristic, including address, weight, citizenship, and family or parental status;\n**(C)**\nidentifiers, including a real name, alias, postal address, unique personal identifier, online identifier, Internet Protocol address, email address, account name, social security number, driver\u2019s license number, passport number, and other similar identifiers;\n**(D)**\ncommercial information, including records of personal property, products or services purchased, obtained, or considered, and other purchasing or consuming histories or tendencies;\n**(E)**\nbiometric data;\n**(F)**\ninternet or other electronic network activity information, including browsing history, search history, and other information regarding interaction by such consumer with a website, application, or advertisement;\n**(G)**\ngeolocation data;\n**(H)**\naudio, electronic, visual, thermal, olfactory, and other similar information;\n**(I)**\nprofessional or employment-related information;\n**(J)**\neducational information, including educational experience, qualifications, and affiliations;\n**(K)**\ninferences drawn from any of the information described in this paragraph and used to create a profile about such consumer reflecting the preferences, characteristics, psychological trends, predispositions, behavior, attitudes, intelligence, abilities, and aptitudes of such consumer;\n**(L)**\ninterests, including the political, personal, and professional affiliation of such consumer;\n**(M)**\nfinancial circumstances, including personal or household wealth, income, property, debt, and credit history; and\n**(N)**\nactions, habits, behaviors, and attributes of such consumer, whether in a physical or digital environment.\n**(9) Pre-dispute arbitration agreement**\nThe term pre-dispute arbitration agreement means any agreement to arbitrate a dispute that has not yet arisen at the time of the making of the agreement.\n**(10) Pre-dispute joint action waiver**\nThe term pre-dispute joint action waiver means an agreement, including as part of a pre-dispute arbitration agreement, that would prohibit, or waive the right of, a party to the agreement from participating in a joint, class, or collective action in a judicial, arbitral, administrative, or other forum, concerning a dispute that has not yet arisen at the time of the making of the agreement.\n**(11) Price**\nThe term price means the amount charged to a consumer in relation to a transaction, including any related cost, fee, and other material term of the transaction that has a direct bearing on the amount paid by the consumer for the item sold or offered for sale to the consumer.\n**(12) Retail food store**\nThe term retail food store has the same meaning given the term in section 3 of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2012 ).\n**(13) Surveillance-based price setting**\nThe term surveillance-based price setting means offering, setting, or informing a customized price for an item for a specific consumer or group of consumers, based, in whole or in part, on personal information collected through electronic surveillance technology, including such information gathered, purchased, or otherwise acquired.",
      "versionDate": "2026-02-12",
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
        "actionDate": "2025-08-12",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4966",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Stop Price Gouging in Grocery Stores Act of 2025",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2026-03-03T20:11:57Z"
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
      "date": "2026-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3892is.xml"
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
      "title": "Stop Price Gouging in Grocery Stores Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-20T11:03:29Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stop Price Gouging in Grocery Stores Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-26T03:53:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit retail food stores from price gouging and engaging in surveillance-based price setting practices, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-26T03:48:24Z"
    }
  ]
}
```
