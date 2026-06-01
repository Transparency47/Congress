# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4361?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4361
- Title: STOP China Act
- Congress: 119
- Bill type: HR
- Bill number: 4361
- Origin chamber: House
- Introduced date: 2025-07-14
- Update date: 2026-05-15T08:07:46Z
- Update date including text: 2026-05-15T08:07:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-14: Introduced in House
- 2025-07-14 - IntroReferral: Introduced in House
- 2025-07-14 - IntroReferral: Introduced in House
- 2025-07-14 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-14 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-15 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-07-14: Introduced in House

## Actions

- 2025-07-14 - IntroReferral: Introduced in House
- 2025-07-14 - IntroReferral: Introduced in House
- 2025-07-14 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-14 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-15 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-14",
    "latestAction": {
      "actionDate": "2025-07-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4361",
    "number": "4361",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "C001087",
        "district": "1",
        "firstName": "Eric",
        "fullName": "Rep. Crawford, Eric A. \"Rick\" [R-AR-1]",
        "lastName": "Crawford",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "STOP China Act",
    "type": "HR",
    "updateDate": "2026-05-15T08:07:46Z",
    "updateDateIncludingText": "2026-05-15T08:07:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-15",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-14",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-14",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-14",
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
          "date": "2025-07-14T16:01:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-07-15T19:34:32Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-07-14T16:01:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "CA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
      "state": "NE"
    },
    {
      "bioguideId": "G000593",
      "district": "28",
      "firstName": "Carlos",
      "fullName": "Rep. Gimenez, Carlos A. [R-FL-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Gimenez",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4361ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4361\nIN THE HOUSE OF REPRESENTATIVES\nJuly 14, 2025 Mr. Crawford (for himself and Mr. Khanna ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo address national security risks and prohibit the use of Federal funds for the procurement of certain vehicles and vehicle technologies produced or provided by entities based in certain countries, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safeguarding Transit Operations to Prohibit China Act or the STOP China Act .\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nthe People\u2019s Republic of China (referred to in this section as the PRC ) uses a deliberately intricate web of industrial policies to distort market behavior to achieve dominance in global markets and increase the dependence of the United States on imports from the PRC;\n**(2)**\nthe adoption of PRC-developed technologies in the United States, including those used in certain vehicles, poses a significant risk to national security and threatens the long-term competitiveness of the United States;\n**(3)**\nthe PRC intentionally creates overcapacity and sells products at below-market prices to gain market share and undermine United States domestic supply chains;\n**(4)**\nCongress must continue to confront the military-civil fusion strategy of the PRC and the intrusion of the PRC into the United States transportation market, as Congress has done in the National Defense Authorization Act for Fiscal Year 2020 ( Public Law 116\u201392 ; 133 Stat. 1198) and the FAA Reauthorization Act of 2024 ( Public Law 118\u201363 ; 138 Stat. 1025);\n**(5)**\nUnited States taxpayer dollars should not be used to fund PRC-subsidized vehicle manufacturing or technology companies; and\n**(6)**\nany entity accepting Federal funding must be prevented from procuring certain vehicles\u2014\n**(A)**\nfrom a PRC entity or an entity otherwise related legally or financially to a corporation based in the PRC; or\n**(B)**\nthat contain certain vehicle technologies identified as matters of national security concern.\n#### 3. Prohibitions relating to certain vehicles produced or provided by entities based in certain countries\nSection 5323(u) of title 49, United States Code, is amended\u2014\n**(1)**\nby striking paragraphs (1) and (2) and inserting the following:\n(1) Definitions In this subsection: (A) Covered entity The term covered entity means an entity (including a corporation, partnership, association, organization, or other entity)\u2014 (i) the principal place of business of which is in a covered nation; (ii) that is headquartered in, incorporated in, or otherwise organized under the laws of a covered nation; (iii) that, regardless of where the entity is organized or doing business, is owned or controlled by a covered nation or covered individual, including circumstances in which a covered individual possesses the power to determine, direct, or decide matters affecting the entity\u2014 (I) through\u2014 (aa) the ownership of a majority of the total outstanding voting interest in the entity; (bb) board representation; (cc) proxy voting; (dd) a special share; (ee) contractual arrangements; (ff) formal or informal arrangements to act in concert; or (gg) other means; and (II) regardless of whether that power is\u2014 (aa) direct; or (bb) exercised or unexercised; (iv) is owned or controlled by, a subsidiary of, an affiliate of, or in a joint venture with an entity described in clause (i), (ii), or (iii); (v) is a manufacturer from which the procurement of rolling stock was ever prohibited under this subsections; or (vi) is an owner of, successor of, subsidiary of, affiliate of, or in a joint venture with a manufacturer described in clause (v). (B) Covered funding The term covered funding means any financial assistance made available under this chapter. (C) Covered individual The term covered individual means any individual, wherever located\u2014 (i) whose activities are directly or supervised, directed, controlled, financed, or subsidized, in whole or in majority part, by a covered nation; (ii) who acts as an agent, representative, or employee of a covered nation or an individual described in clause (i); (iii) who acts in any other capacity at the order of, at the request of, or under the direction or control of a covered nation or an individual described in clause (i); or (iv) who\u2014 (I) is a citizen or resident of a covered nation or a country controlled by a covered nation; and (II) is not a citizen or permanent resident of the United States. (D) Covered nation The term covered nation has the meaning given the term in section 4872(d) of title 10. (E) Covered vehicle The term covered vehicle means rolling stock that\u2014 (i) is produced or provided by a covered entity included on the list developed under paragraph (2)(B); or (ii) incorporates an electric power train produced or provided by a covered entity included on the list developed under paragraph (2)(B). (F) Electric power train The term electric power train has the meaning given the term in section 571.305 of title 49, Code of Federal Regulations (as in effect on the date of enactment of the STOP China Act ). (2) Prohibition (A) In general Subject to subparagraph (C), on and after the date of enactment of the STOP China Act , the Secretary may not award or obligate covered funding\u2014 (i) for a contract or subcontract for the procurement of a covered vehicle; or (ii) for the construction, installation, or maintenance of infrastructure to fuel or charge a covered vehicle that is a bus, if the applicable covered vehicle is procured under a contract or subcontract executed on or after the date of enactment of the STOP China Act . (B) List of covered entities (i) In general Not later than 30 days after the date of enactment of the STOP China Act , the United States Trade Representative, in consultation with the Attorney General and the Secretary, shall make publicly available, including on a publicly accessible website, a list of covered entities that produce or provide\u2014 (I) rolling stock to which the prohibition under subparagraph (A) applies; or (II) electric power trains the incorporation of which into rolling stock would render the rolling stock subject to the prohibition under subparagraph (A). (ii) Updates The United States Trade Representative shall update the list required under clause (i)\u2014 (I) based on information provided to the United States Trade Representative by the Attorney General and the Secretary; and (II) not less frequently than\u2014 (aa) once every 90 days during the 180-day period beginning on the date of initial publication of the list under that clause; and (bb) annually thereafter. (C) Exception Notwithstanding subparagraph (A), the Secretary may procure a covered vehicle or construct, install, or maintain infrastructure to fuel or charge a covered vehicle for purposes of\u2014 (i) the inspection or investigation of a motor vehicle or equipment; or (ii) motor vehicle safety research, development, or testing. .\n**(2)**\nin paragraph (4), by striking paragraph (1) each place that term appears and inserting paragraph (2) ;\n**(3)**\nin paragraph (5)\u2014\n**(A)**\nin subparagraph (A)\u2014\n**(i)**\nby striking This subsection, including the and inserting The ;\n**(ii)**\nby striking the comma after (4) ;\n**(iii)**\nby inserting that does not utilize covered funds after subcontract ;\n**(iv)**\nby striking rail rolling stock manufacturer described in paragraph (1) and inserting covered entity ;\n**(v)**\nby striking the manufacturer and inserting the covered entity ; and\n**(vi)**\nby striking date of enactment of this subsection and inserting date of enactment of the STOP China Act ;\n**(B)**\nby striking subparagraph (B) and inserting the following:\n(B) Contract completion Notwithstanding paragraph (2), covered funds may be obligated for a contract or subcontract that was eligible for assistance under this chapter under the provisions of this subsection prior to the date of enactment of the STOP China Act until the delivery of rolling stock is complete under such contract. ; and\n**(C)**\nby striking subparagraph (C); and\n**(4)**\nby adding at the end the following:\n(6) Severability If any provision of this subsection, or the application of this subsection to any person or circumstance, is held to be unconstitutional or otherwise invalid, the remainder of this subsection, and the application of the provision to any other person or circumstance, shall not be affected. .\n#### 4. Prohibitions relating to additional vehicles produced or provided by entities based in certain countries\n##### (a) Definitions\nIn this section:\n**(1) Covered entity; covered individual; covered nation; covered vehicle; electric power train**\nThe terms covered entity ; covered individual , covered nation , covered vehicle , and electric power train have the meanings given those terms in section 5323(u)(1) of title 49, United States Code.\n**(2) Covered funding**\nThe term covered funding means any appropriations made available to the Department, other than funds made available under chapter 53 of title 49, United States Code.\n**(3) Department**\nThe term Department means the Department of Transportation.\n**(4) Secretary**\nThe term Secretary means the Secretary of Transportation.\n##### (b) Prohibition\n**(1) In general**\nSubject to paragraph (3), the Department may not award, obligate, allocate, or expend covered funding\u2014\n**(A)**\nfor the procurement of a covered vehicle by the Department or any other agency or person; or\n**(B)**\nfor the construction, installation, or maintenance of infrastructure to fuel or charge a covered vehicle that is a bus, if the applicable covered vehicle is procured under a contract or subcontract executed on or after the date of enactment of this Act.\n**(2) List of covered entities**\n**(A) In general**\nNot later than 30 days after the date of enactment of this Act, the United States Trade Representative, in consultation with the Attorney General and the Secretary, shall make publicly available, including on a publicly accessible website, a list of covered entities that produce or provide\u2014\n**(i)**\ncovered vehicles to which the prohibition under paragraph (1) applies; or\n**(ii)**\nelectric power trains the incorporation of which into a covered vehicle would render the covered vehicle subject to the prohibition under that paragraph.\n**(B) Updates**\nThe United States Trade Representative shall update the list required under subparagraph (A)\u2014\n**(i)**\nbased on information provided to the United States Trade Representative by the Attorney General and the Secretary; and\n**(ii)**\nnot less frequently than\u2014\n**(I)**\nonce every 90 days during the 180-day period beginning on the date of initial publication of the list under that subparagraph; and\n**(II)**\nannually thereafter.\n**(3) Exception**\nNotwithstanding paragraph (1), the Department may procure a covered vehicle or construct, install, or maintain infrastructure to fuel or charge a covered vehicle for purposes of\u2014\n**(A)**\nthe inspection or investigation of a motor vehicle or equipment; or\n**(B)**\nmotor vehicle safety research, development, or testing.\n##### (c) Severability\nIf any provision of this section, or the application of this section to any person or circumstance, is held to be unconstitutional or otherwise invalid, the remainder of this section, and the application of the provision to any other person or circumstance, shall not be affected.",
      "versionDate": "2025-07-14",
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
        "actionDate": "2025-05-12",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "1711",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "STOP China Act",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-09-04T14:55:11Z"
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
      "date": "2025-07-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4361ih.xml"
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
      "title": "STOP China Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-24T05:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "STOP China Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-24T05:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Safeguarding Transit Operations to Prohibit China Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-24T05:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To address national security risks and prohibit the use of Federal funds for the procurement of certain vehicles and vehicle technologies produced or provided by entities based in certain countries, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-24T05:18:44Z"
    }
  ]
}
```
