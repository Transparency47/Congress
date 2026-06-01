# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5875?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5875
- Title: COWS Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5875
- Origin chamber: House
- Introduced date: 2025-10-31
- Update date: 2026-03-05T09:06:53Z
- Update date including text: 2026-03-05T09:06:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-31: Introduced in House
- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2025-10-31: Introduced in House

## Actions

- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-31",
    "latestAction": {
      "actionDate": "2025-10-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5875",
    "number": "5875",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "C001059",
        "district": "21",
        "firstName": "Jim",
        "fullName": "Rep. Costa, Jim [D-CA-21]",
        "lastName": "Costa",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "COWS Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-05T09:06:53Z",
    "updateDateIncludingText": "2026-03-05T09:06:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-31",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-10-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-31",
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
          "date": "2025-10-31T17:05:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "CA"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "ME"
    },
    {
      "bioguideId": "G000605",
      "district": "13",
      "firstName": "Adam",
      "fullName": "Rep. Gray, Adam [D-CA-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Gray",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "CA"
    },
    {
      "bioguideId": "M001231",
      "district": "22",
      "firstName": "John",
      "fullName": "Rep. Mannion, John W. [D-NY-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Mannion",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5875ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5875\nIN THE HOUSE OF REPRESENTATIVES\nOctober 31, 2025 Mr. Costa (for himself, Mr. Valadao , Ms. Pingree , and Mr. Gray ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo provide for the reform and continuation of agricultural and other programs of the Department of Agriculture through fiscal year 2029, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Converting Our Waste Sustainably Act of 2025 or the COWS Act of 2025 .\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nthe Alternative Manure Management Program (AMMP) is a successful program in California that supports the livestock industry and is an example of what can be done nationally in the United States through a variety of practices on responsible manure management;\n**(2)**\nthe 195 existing projects under AMMP are contributing towards the reduction of 1,600,000 metric tons of greenhouse gases; and\n**(3)**\nthese practices enhance sustainability and nurture continued environmental stewardship, ultimately leading to enhanced local air quality and recycled manure for use as a natural fertilizer or compost for healthier soil.\n#### 3. Definitions\n##### (a) Composting practice\nSection 1201(a) of the Food Security Act of 1985 ( 16 U.S.C. 3801(a) ) is amended\u2014\n**(1)**\nby redesignating paragraphs (3) through (27) as paragraphs (4) through (28), respectively; and\n**(2)**\nby inserting after paragraph (2) the following:\n(3) Composting practice The term composting practice means an activity (including an activity that does not require the use of a composting facility) to produce compost from organic waste that is\u2014 (A) generated on a farm; or (B) brought to a farm from the nearby community; and (C) the use and active management of compost on a farm to improve water retention and soil health, subject to the condition that such use shall be in compliance with applicable Federal, State, and local laws. .\n##### (b) Alternative manure management\nSection 1240A of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u20131 ) is amended\u2014\n**(1)**\nby redesignating paragraphs (1) through (10) as paragraphs (2) through (11), respectively; and\n**(2)**\nby inserting before paragraph (2), as so redesignated, the following:\n(1) Alternative manure management practices The term alternative manure management practices means management measures that reduce baseline methane and nitrous oxide emissions and, where applicable, reduce nitrate leaching into groundwater or improve carbon sequestration, including\u2014 (A) converting to or improving pasture-based management, including management-intensive rotational grazing (as defined in section 1240L(d)(1)); (B) compost-bedded pack barns that compost manure, slatted floor pit storage that is cleaned out at least once a month, or other similar practices as determined by the Secretary; and (C) solid separation, scrape and vacuum technologies, or other measures, including manure management system retrofits, that primarily avoid wet handling and storage infrastructure in conjunction with\u2014 (i) open or enclosed solar drying; (ii) composting; (iii) vermiculture or vermifiltration; (iv) forced evaporation; (v) solid storage; or (vi) other similar methods as determined by the Secretary. .\n##### (c) Practice\nSubparagraph (A) of section 1240A(7) of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u20131(7) ), as so redesignated by subsection (a), is amended\u2014\n**(1)**\nin clause (ii), by inserting and composting practices after practices ;\n**(2)**\nin clause (vi), by striking the and at the end;\n**(3)**\nby redesignating clause (vii) as clause (ix); and\n**(4)**\nby inserting after clause (vi) the following:\n(vii) composting practices; (viii) alternative manure management practices; and .\n##### (d) Inclusions\nSection 1240I(2)(B)(i) of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u201321(2)(B)(i) ) is amended by inserting and composting practices after drainage management systems .\n#### 4. Establishment and administration\n##### (a) Increased payments for high-Priority practices\nSection 1240B(d)(7) of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u20132(d)(7) ) is amended\u2014\n**(1)**\nin the paragraph heading, by inserting state-determined before high-priority ; and\n**(2)**\nin subparagraph (A)\u2014\n**(A)**\nin clause (iii), by striking or at the end;\n**(B)**\nin clause (iv), by striking the period at the end and inserting ; or ; and\n**(C)**\nby adding at the end the following:\n(v) increases carbon sequestration or reduces greenhouse gas emissions, including emissions of methane and nitrous oxide. .\n##### (b) Livestock\nSection 1240B(f)(1) of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u20132(f)(1) ) is amended by inserting and alternative manure management after including grazing management .\n##### (c) Alternative manure management practices\nSection 1240B of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u20132 ) is amended\u2014\n**(1)**\nby redesignating subsections (h) through (j) as subsection (i) through (k), respectively; and\n**(2)**\nby inserting after subsection (g) the following:\n(h) Alternative Manure Management Practices (1) Payment amounts The Secretary may provide a payment for an alternative manure management practice for an amount that is up to 100 percent of the costs associated with planning, design, materials, equipment, installation, labor, management, maintenance, and training related to implementing a covered management measure. (2) Advanced payments The Secretary shall provide at least 50 percent of the amount of total payments for an alternative manure management practice in advance for all costs related to\u2014 (A) purchasing or contracting materials and equipment; or (B) any technical assistance provided by the Secretary. (3) Term A contract awarded under this section shall have a term that does not exceed 3 years. .\n#### 5. Prioritization of applications\nSection 1240C(b) of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u20133(b) ) is amended\u2014\n**(1)**\nby redesignating paragraphs (1) through (4) as subparagraphs (A) through (D), respectively, and by indenting such subparagraphs 2 ems to the right;\n**(2)**\nin the matter preceding subparagraph (A), as redesignated by paragraph (1), by striking In evaluating applications under this subchapter, the Secretary shall prioritize applications\u2014 and inserting the following:\n(1) In general In evaluating applications under this subchapter, the Secretary shall prioritize applications\u2014 ; and\n**(3)**\nby adding at the end the following:\n(2) Alternative manure management applications (A) In general The Secretary shall develop criteria for evaluating and ranking alternative manure management contract offers to prioritize applications that will maximize\u2014 (i) carbon sequestration; (ii) greenhouse gas emissions reductions; and (iii) the overall environmental and public health benefits, including improved water quality and quantity. (B) Additional criteria In awarding alternative manure management applications, the Secretary shall develop criteria to ensure\u2014 (i) geographical diversity; (ii) scale diversity, including support for small and medium sized dairy and livestock operations; and (iii) participation by operations with a demonstrated track record of adopting conservation measures and reducing greenhouse gas emissions. (C) Cluster applications The Secretary shall establish procedures under which\u2014 (i) a group of producers may submit a joint application for a shared composting facility; and (ii) the Secretary allocates payments to each eligible producer associated with that joint contract. (D) Serving certain producers To the maximum extent practicable, the Secretary shall award the majority of alternative manure contracts finalized each fiscal year to offers from small and mid-sized dairy and livestock operations, including\u2014 (i) beginning farmers or ranchers; (ii) limited resource farmers and ranchers; and (iii) socially disadvantaged farmers and ranchers. .\n#### 6. Duties of the Secretary\nSection 1240F of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u20136 ) is amended by\u2014\n**(1)**\ninserting (a) In general.\u2014 before To the extent appropriate, the Secretary shall assist a producer in achieving the conservation and environmental goals of a program plan by\u2014 ; and\n**(2)**\ninserting at the end the following:\n(b) Alternative manure management For alternative manure management contracts, the Secretary shall\u2014 (1) determine and publish factors for estimating the carbon sequestrations and greenhouse gas emissions reductions for each alternative manure management practice; (2) identify eligible producers based on manure management practices used at the time of application, including the anaerobic decomposition of volatile solids stored in a lagoon or other predominantly liquid anaerobic environment and their ability to replace or complement that anaerobic system with an alternative manure management practice; and (3) assist an eligible producer in achieving the carbon sequestration, greenhouse gas emissions reduction, and other environmental and public health goals of the alternative manure management systems by\u2014 (A) providing payments for designing and implementing one or more alternative manure management practices; (B) providing that eligible producer with information, technical assistance, and training to aid in implementation of the alternative manure management practices; (C) reviewing the adequacy of existing conservation practice standards for supporting the alternative manure management practices and, if necessary\u2014 (i) revising existing conservation practice standards; and (ii) developing new conservation practice standards; and (D) entering into cooperative agreements with third-party technical assistance providers with relevant expertise in alternative manure management systems to ensure adequate technical services are available to alternative manure management applicants. .\n#### 7. Limitation on payments\nSection 1240G of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u20137 ) is amended\u2014\n**(1)**\nby inserting (a) In general.\u2014 before Not including payments ; and\n**(2)**\nby striking , regardless of the number of contracts entered into under this subchapter by the person or legal entity and inserting at the end the following:\n(b) Waiver authority and limitation The Secretary may\u2014 (1) waive the applicability of the limitations in section 1001D(b) or section 1240(G) for a payment made under an alternative manure management contract if the Secretary determines that the waiver is necessary to fulfill the objectives of the project; and (2) impose a separate payment limitation for the contract with respect to which the waiver applies. .\n#### 8. New or innovative conservation approach\nSection 1240H(c)(1)(B)(i) of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u20138(c)(1)(B)(i) ) is amended\u2014\n**(1)**\nin subclause (VI), by striking and at the end; and\n**(2)**\nby inserting at the end the following:\n(VIII) alternative manure management practices; and .\n#### 9. Delivery of technical assistance\nSection 1242(h) of the Food Security Act of 1985 ( 16 U.S.C. 3842(h) ) is amended by adding at the end the following:\n(5) Development of composting practice standard Not later than one year after the date of enactment of this paragraph, the Secretary shall\u2014 (A) conduct a review of the composting facilities practice standard and the soil carbon amendment practice standard to determine their adequacy in advancing alternative manure management and on-farm composting generation and utilization; and (B) develop and implement a new conservation practice standard for the on-farm production of compost. .",
      "versionDate": "2025-10-31",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-11-25T16:48:14Z"
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
      "date": "2025-10-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5875ih.xml"
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
      "title": "COWS Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-13T09:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "COWS Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-13T09:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Converting Our Waste Sustainably Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-13T09:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for the reform and continuation of agricultural and other programs of the Department of Agriculture through fiscal year 2029, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-13T09:48:14Z"
    }
  ]
}
```
