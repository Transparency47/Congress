# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8510?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8510
- Title: PRICE Act
- Congress: 119
- Bill type: HR
- Bill number: 8510
- Origin chamber: House
- Introduced date: 2026-04-27
- Update date: 2026-05-12T12:31:36Z
- Update date including text: 2026-05-12T12:31:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-27: Introduced in House
- 2026-04-27 - IntroReferral: Introduced in House
- 2026-04-27 - IntroReferral: Introduced in House
- 2026-04-27 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-04-27: Introduced in House

## Actions

- 2026-04-27 - IntroReferral: Introduced in House
- 2026-04-27 - IntroReferral: Introduced in House
- 2026-04-27 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-27",
    "latestAction": {
      "actionDate": "2026-04-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8510",
    "number": "8510",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "G000599",
        "district": "10",
        "firstName": "Daniel",
        "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
        "lastName": "Goldman",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "PRICE Act",
    "type": "HR",
    "updateDate": "2026-05-12T12:31:36Z",
    "updateDateIncludingText": "2026-05-12T12:31:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-27",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-27",
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
          "date": "2026-04-27T16:01:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "VA"
    },
    {
      "bioguideId": "H001103",
      "district": "0",
      "firstName": "Pablo",
      "fullName": "Rescom. Hern\u00e1ndez, Pablo Jose [D-PR-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Hern\u00e1ndez",
      "middleName": "Jose",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "PR"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "DC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8510ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8510\nIN THE HOUSE OF REPRESENTATIVES\nApril 27, 2026 Mr. Goldman of New York (for himself, Mr. Subramanyam , Mr. Hern\u00e1ndez , and Ms. Norton ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo require third-party delivery platforms to follow certain pricing practices, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Promoting Real-time Information on Cost Expenditure Act or the PRICE Act .\n#### 2. Definitions\nIn this Act:\n**(1) Commission**\nThe term Commission means the Federal Trade Commission.\n**(2) Delivery fee**\nThe term delivery fee means any fee imposed by a third-party delivery platform on a user of the platform with respect to an order placed through the platform of items from a retail establishment that is in addition to any charge that the retail establishment would impose on the sale of the same items if they were purchased by an individual who is physically present in such establishment. In the case of a retail establishment that does not offer items for sale to individuals who are physically present in such establishment, such term shall include any fee imposed by a third-party delivery platform that is in addition to the menu or retail price for the items ordered.\n**(3) Retail establishment**\nThe term retail establishment means a physical establishment (including a restaurant) where items (including food, beverages, or other goods) are offered for sale to individuals who\u2014\n**(A)**\nare physically present in such establishment; or\n**(B)**\nplace orders through a third-party delivery platform.\n**(4) Third-party delivery platform**\nThe term third-party delivery platform means any website, mobile application, or other internet service that\u2014\n**(A)**\nas its primary function, offers or arranges for the sale and same-day delivery of items (including food beverages, or other goods) from a retail establishment; and\n**(B)**\nis not owned by, under common ownership with, operated by, or a subsidiary of the retail establishment.\n#### 3. Pricing requirements for third-party delivery platforms\n##### (a) In general\nBeginning 90 days after the date of enactment of this Act, it shall be unlawful to operate a third-party delivery platform unless such platform satisfies the requirements described in subsection (b).\n##### (b) Pricing requirements\nThe requirements described in this subsection, with respect to a third-party delivery platform, are the following:\n**(1)**\nIf the third-party delivery platform charges 1 or more delivery fees for an order from a retail establishment, any such delivery fee shall be\u2014\n**(A)**\ncalculated using a methodology that is determined no later than the time the user placing the order selects the retail establishment and may not change once the user has begun their order from the retail establishment; and\n**(B)**\nbased solely on\u2014\n**(i)**\nthe total price charged by the retail establishment for items ordered by the user, excluding any taxes and any fees imposed by the third-party delivery platform; and\n**(ii)**\nother factors related to the delivery of the items ordered from the retail establishment, including the delivery distance, but excluding\u2014\n**(I)**\nany other factor that directly or indirectly relies on, incorporates, or is informed by variables that serve as a proxy for characteristics of the user placing the order or a class of users, including inferred price sensitivity, prior purchasing behavior, or willingness to pay; and\n**(II)**\nany factor related to an arrangement negotiated between the third-party delivery platform and the retail establishment.\n**(2)**\nWhenever a user selects an item to order from a retail establishment through the third-party delivery platform, the third-party delivery platform shall prominently display\u2014\n**(A)**\nthe price charged by the retail establishment for such item, excluding any taxes; and\n**(B)**\nif applicable, any delivery fees imposed with respect to such item by the third-party delivery platform.\n**(3)**\nThroughout the ordering process, the third-party delivery platform shall prominently display the ongoing total amount to be charged to the user for the order that includes every item that the user has selected up to that point. Such total amount shall include the cost of each item selected, applicable taxes, and any applicable fees.\n**(4)**\nPrior to requesting payment for an order, the third-party delivery platform shall provide the user with an explanation, in a clear, conspicuous, and not misleading manner, of each delivery fee imposed on the user by the platform and what the fee is for. Such explanation shall include the amount of the delivery fee, the item that the delivery fee relates to, whether the delivery fee is refundable, and such other information as the Commission may specify.\n##### (c) Rule of construction regarding gratuities\nNothing in this section shall be construed to prevent a third-party delivery platform from allowing a user to add a gratuity to their order.\n#### 4. Enforcement\n##### (a) Enforcement by the Federal Trade Commission\n**(1) Unfair and deceptive acts or practices**\nA violation of this Act shall be treated as a violation of a rule defining an unfair or deceptive act or practice prescribed under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n**(2) Powers of the Commission**\n**(A) In general**\nThe Commission shall enforce this Act in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this Act.\n**(B) Privileges and immunities**\nAny person that violates this Act shall be subject to the penalties, and entitled to the privileges and immunities, provided in the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ).\n**(C) Regulations**\nThe Commission shall, pursuant to section 553 of title 5, United States Code promulgate such regulations as the Commission determines necessary to carry out the provisions of this Act.\n**(D) Authority preserved**\nNothing in this Act shall be construed to limit the authority of the Commission under any other provision of law.\n##### (b) Enforcement by State attorneys general\n**(1) In general**\n**(A) Civil actions**\nIn any case in which the attorney general of a State has reason to believe that an interest of the residents of that State has been or is threatened or adversely affected by the engagement of any person in a practice that violates this Act, the State, as parens patriae, may bring a civil action on behalf of the residents of the State in a district court of the United States or a State court of appropriate jurisdiction to\u2014\n**(i)**\nenjoin that practice;\n**(ii)**\nenforce compliance with this Act or such regulation;\n**(iii)**\non behalf of residents of the State, obtain damages, restitution, or other compensation, each of which shall be distributed in accordance with State law; or\n**(iv)**\nobtain such other relief as the court may consider to be appropriate.\n**(B) Notice**\n**(i) In general**\nBefore filing an action under subparagraph (A), the attorney general of the State involved shall provide to the Commission\u2014\n**(I)**\nwritten notice of that action; and\n**(II)**\na copy of the complaint for that action.\n**(ii) Exemption**\n**(I) In general**\nClause (i) shall not apply with respect to the filing of an action by an attorney general of a State under this paragraph if the attorney general of the State determines that it is not feasible to provide the notice described in that clause before the filing of the action.\n**(II) Notification**\nIn an action described in subclause (I), the attorney general of a State shall provide notice and a copy of the complaint to the Commission at the same time as the attorney general files the action.\n**(2) Intervention**\n**(A) In general**\nOn receiving notice under paragraph (1)(B), the Commission shall have the right to intervene in the action that is the subject of the notice.\n**(B) Effect of intervention**\nIf the Commission intervenes in an action under paragraph (1), it shall have the right\u2014\n**(i)**\nto be heard with respect to any matter that arises in that action; and\n**(ii)**\nto file a petition for appeal.\n**(3) Construction**\nFor purposes of bringing any civil action under paragraph (1), nothing in this Act shall be construed to prevent an attorney general of a State from exercising the powers conferred on the attorney general by the laws of that State to\u2014\n**(A)**\nconduct investigations;\n**(B)**\nadminister oaths or affirmations; or\n**(C)**\ncompel the attendance of witnesses or the production of documentary and other evidence.\n**(4) Actions by the commission**\nIn any case in which an action is instituted by or on behalf of the Commission for violation of this Act, no State may, during the pendency of that action, institute a separate action under paragraph (1) against any defendant named in the complaint in the action instituted by or on behalf of the Commission for that violation.\n**(5) Venue; service of process**\n**(A) Venue**\nAny action brought under paragraph (1) may be brought in\u2014\n**(i)**\nthe district court of the United States that meets applicable requirements relating to venue under section 1391 of title 28, United States Code; or\n**(ii)**\na State court of competent jurisdiction.\n**(B) Service of process**\nIn an action brought under paragraph (1) in a district court of the United States, process may be served wherever defendant\u2014\n**(i)**\nis an inhabitant; or\n**(ii)**\nmay be found.",
      "versionDate": "2026-04-27",
      "versionType": "Introduced in House"
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
        "actionDate": "2026-04-27",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "4401",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "PRICE Act",
      "type": "S"
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
        "updateDate": "2026-05-06T20:50:52Z"
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
      "date": "2026-04-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8510ih.xml"
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
      "title": "PRICE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-05T13:08:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PRICE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-05T13:08:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Promoting Real-time Information on Cost Expenditure Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-05T13:08:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require third-party delivery platforms to follow certain pricing practices, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-05T13:03:30Z"
    }
  ]
}
```
