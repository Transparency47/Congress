# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3955?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3955
- Title: RAPID Reserve Act
- Congress: 119
- Bill type: HR
- Bill number: 3955
- Origin chamber: House
- Introduced date: 2025-06-12
- Update date: 2026-01-14T05:02:30Z
- Update date including text: 2026-01-14T05:02:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-12: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-06-12: Introduced in House

## Actions

- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-12",
    "latestAction": {
      "actionDate": "2025-06-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3955",
    "number": "3955",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001119",
        "district": "2",
        "firstName": "Angie",
        "fullName": "Rep. Craig, Angie [D-MN-2]",
        "lastName": "Craig",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "RAPID Reserve Act",
    "type": "HR",
    "updateDate": "2026-01-14T05:02:30Z",
    "updateDateIncludingText": "2026-01-14T05:02:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-12",
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
      "actionDate": "2025-06-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-12",
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
          "date": "2025-06-12T14:06:30Z",
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
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3955ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3955\nIN THE HOUSE OF REPRESENTATIVES\nJune 12, 2025 Ms. Craig (for herself and Mr. Van Drew ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo improve supply chain resiliency for critical drug products with vulnerable supply chains and ensure that reserves of critical drugs and active pharmaceutical ingredients are maintained to prevent supply disruptions in the event of drug shortages or public health emergencies.\n#### 1. Short title\nThis Act may be cited as the Rolling Active Pharmaceutical Ingredient and Drug Reserve Act or the RAPID Reserve Act .\n#### 2. Rolling active pharmaceutical ingredient and drug reserve\n##### (a) In general\nThe Secretary of Health and Human Services (referred to in this section as the Secretary ) shall award contracts or cooperative agreements to eligible entities with respect to drugs and active pharmaceutical ingredients of such drugs that the Secretary determines to be critical and to have vulnerable supply chains. The Secretary shall publish the list of such drugs and active pharmaceutical ingredients of such drugs.\n##### (b) Requirements\n**(1) In general**\nAn eligible entity, pursuant to a contract or cooperative agreement under subsection (a), shall agree to\u2014\n**(A)**\nmaintain, in a satisfactory domestic establishment registered under section 510(b) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 360(b) ) or in a satisfactory foreign establishment registered under section 510(i) of such Act that is located in a country that is a member of the Organisation for Economic Cooperation and Development, which may be an establishment owned and operated by the entity, or by a wholesaler, distributor, or other third party under contract with the entity, a 6-month reserve, or other reasonable quantity, as determined by the Secretary, of\u2014\n**(i)**\nthe active pharmaceutical ingredient of the eligible drug specified in the contract or cooperative agreement, which reserve shall be regularly replenished with a recently manufactured supply of such ingredient; and\n**(ii)**\nthe finished eligible drug product specified in the contract or cooperative agreement, which reserve shall be regularly replenished with a recently manufactured supply of such product;\n**(B)**\nimplement production of the eligible drug or an active pharmaceutical ingredient of the eligible drug, at the direction of the Secretary, under the terms of, and in such quantities as specified in, the contract or cooperative agreement; and\n**(C)**\nenter into an arrangement with the Secretary under which the eligible entity\u2014\n**(i)**\nagrees to transfer a portion, as determined necessary, of the reserve of active pharmaceutical ingredient maintained pursuant to subparagraph (A)(i) to another drug manufacturer in the event that the Secretary determines there to be a need for additional finished eligible drug product and such eligible entity is unable to use the reserve of active pharmaceutical ingredient to manufacture a sufficient supply of such drug product; and\n**(ii)**\npermits the Secretary to direct allocation of the reserve of active pharmaceutical ingredient so maintained in the event of a public health emergency, natural disaster, or chemical, biological, radiological, or nuclear threat.\n**(2) Guidance**\nNot later than 180 days after the date of enactment of this Act, the Secretary, in coordination with the Commissioner of Food and Drugs, shall issue guidance on\u2014\n**(A)**\nthe factors the Secretary will use to determine which eligible drugs, or active pharmaceutical ingredient of such drugs, have vulnerable supply chains and how a contract or cooperative agreement would help minimize the vulnerability or vulnerabilities identified;\n**(B)**\nthe factors the Secretary will consider in determining eligibility of an entity to participate in the program under this section, which shall include an entity\u2019s commitment to quality systems, including strong manufacturing infrastructure, reliable processes, and trained staff, as well as the entity\u2019s commitment to domestic manufacturing capacity and surge capacity, as appropriate; and\n**(C)**\nrequirements for entities receiving an award under this section, including the extent of excess manufacturing capacity the manufacturers will be required to generate, the amount of redundancy required, and requirements relating to advanced quality systems.\n**(3) Preference**\nIn awarding contracts and cooperative agreements under subsection (a), the Secretary shall\u2014\n**(A)**\ngive preference to eligible entities that will\u2014\n**(i)**\ncarry out the requirements of paragraph (1) through one or more domestic establishments registered under section 510(b) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 360(b) ) capable of manufacturing the eligible drug; or\n**(ii)**\nsource key starting materials or excipients for eligible drugs domestically or from a country that is a member of the Organisation for Economic Cooperation and Development; and\n**(B)**\nto the greatest extent practicable, award such contracts and cooperative agreements in a manner that strengthens domestic manufacturing, resiliency, and capacity of eligible drugs and their active pharmaceutical ingredients.\n##### (c) Additional contract and cooperative agreement terms\n**(1) In general**\nEach contract or cooperative agreement under subsection (a) shall be subject to such terms and conditions as the Secretary may specify, including terms and conditions with respect to procurement, maintenance, storage, testing, and delivery of drugs, in alignment with inventory management and other applicable best practices, under such contract or cooperative agreement, which may consider, as appropriate, costs of transporting and handling such drugs.\n**(2) Terms concerning the acquisition, construction, alteration, or renovation of establishments**\nNotwithstanding section 6303 of title 41, United States Code, the Secretary may award a contract or cooperative agreement under this section to support the acquisition, construction, alteration, or renovation of non-federally owned establishments\u2014\n**(A)**\nas determined necessary to carry out or improve preparedness and response capability at the State and local level; or\n**(B)**\nfor the production of drugs, devices, and supplies where the Secretary determines that such a contract or cooperative agreement is necessary to ensure sufficient amounts of such drugs, devices, and supplies.\n##### (d) Requirements in awarding contracts\nTo the greatest extent practicable, the Secretary shall award contracts and cooperative agreements under this section in a manner that\u2014\n**(1)**\nmaximizes quality, minimizes cost, minimizes vulnerability of the United States to severe shortages or disruptions for eligible drugs and their active pharmaceutical ingredients, gives preference to domestic manufacturers, and encourages competition in the marketplace; and\n**(2)**\nincreases domestic production surge capacity and reserves of domestic-based manufacturing establishments for critical drugs and active pharmaceutical ingredients of such drugs.\n##### (e) Definitions\nIn this section:\n**(1) Active pharmaceutical ingredient**\nThe term active pharmaceutical ingredient has the meaning given such term in section 744A of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 379j\u201341 ).\n**(2) Drug**\nThe term drug has the meaning given such term in section 201(g) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321(g) ).\n**(3) Drug shortage; shortage**\nThe term drug shortage or shortage has the meaning given such term in section 506C of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 356c ).\n**(4) Eligible drug**\nThe term eligible drug means a drug, as determined by the Secretary, in coordination with the Assistant Secretary for Preparedness and Response, the Director of the Centers for Disease Control and Prevention, and the Commissioner of Food and Drugs\u2014\n**(A)**\nthat is approved under section 505(j) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(j) ) or licensed under section 351(k) of the Public Health Service Act ( 42 U.S.C. 262(k) );\n**(B)**\n**(i)**\nthat is reasonably likely to be required to respond to a public health emergency or to a chemical, biological, radiological, or nuclear threat; or\n**(ii)**\nthe shortage of which would pose a significant threat to the United States health care system or at-risk populations; and\n**(C)**\nthat has a vulnerable supply chain, such as a geographic concentration of manufacturing, poor quality or safety issues, complex manufacturing or chemistry, or few manufacturers.\n**(5) Eligible entity**\nThe term eligible entity means a person that\u2014\n**(A)**\n**(i)**\nis the holder of an approved application under subsection (j) of section 505 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355 ) or subsection (k) of section 351 of the Public Health Service Act ( 42 U.S.C. 262 ) for an eligible drug;\n**(ii)**\nmaintains at least one domestic establishment registered under section 510(b) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 360(b) ) or one foreign establishment registered under section 510(i) of such Act that is located in a country that is a member of the Organisation for Economic Cooperation and Development that is capable of manufacturing the eligible drug; and\n**(iii)**\nhas a strong record of good manufacturing practices of drugs;\n**(B)**\n**(i)**\nis a manufacturer of an active pharmaceutical ingredient for an eligible drug, in partnership with an entity that meets the requirements of subparagraph (A);\n**(ii)**\nmaintains at least one domestic establishment registered under section 510(b) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 360(b) ) or one foreign establishment registered under section 510(i) of such Act that is located in a country that is a member of the Organisation for Economic Cooperation and Development that is capable of manufacturing the active pharmaceutical ingredient; and\n**(iii)**\nhas a strong record of good manufacturing practices of active pharmaceutical ingredients; or\n**(C)**\nis a distributor or wholesaler of an eligible drug, in partnership with an entity that meets the requirements of subparagraph (A).\n##### (f) Reports to Congress\nNot later than 2 years after the date on which the first award is made under this section, and every 2 years thereafter, the Secretary shall submit a report to Congress detailing\u2014\n**(1)**\nthe list of drugs determined to be eligible drugs, as described in subsection (e)(2), and the rationale behind selecting each such drug; and\n**(2)**\nan update on the effectiveness of the program under this section, in a manner that does not compromise national security.\n##### (g) Authorization of appropriations\nTo carry out this section, there is authorized to be appropriated $500,000,000 for fiscal year 2026.",
      "versionDate": "2025-06-12",
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
        "actionDate": "2025-06-12",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "2062",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "RAPID Reserve Act",
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
        "name": "Health",
        "updateDate": "2025-07-02T18:06:17Z"
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
      "date": "2025-06-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3955ih.xml"
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
      "title": "RAPID Reserve Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-19T03:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "RAPID Reserve Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-19T03:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Rolling Active Pharmaceutical Ingredient and Drug Reserve Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-19T03:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To improve supply chain resiliency for critical drug products with vulnerable supply chains and ensure that reserves of critical drugs and active pharmaceutical ingredients are maintained to prevent supply disruptions in the event of drug shortages or public health emergencies.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-19T03:33:29Z"
    }
  ]
}
```
