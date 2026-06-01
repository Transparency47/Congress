# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6143?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6143
- Title: PRECISE Act
- Congress: 119
- Bill type: HR
- Bill number: 6143
- Origin chamber: House
- Introduced date: 2025-11-19
- Update date: 2026-05-08T08:05:50Z
- Update date including text: 2026-05-08T08:05:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-19: Introduced in House
- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2025-11-19: Introduced in House

## Actions

- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-19",
    "latestAction": {
      "actionDate": "2025-11-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6143",
    "number": "6143",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "H001091",
        "district": "2",
        "firstName": "Ashley",
        "fullName": "Rep. Hinson, Ashley [R-IA-2]",
        "lastName": "Hinson",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "PRECISE Act",
    "type": "HR",
    "updateDate": "2026-05-08T08:05:50Z",
    "updateDateIncludingText": "2026-05-08T08:05:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-19",
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
      "actionDate": "2025-11-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-19",
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
          "date": "2025-11-19T15:00:30Z",
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
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "CA"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "MN"
    },
    {
      "bioguideId": "G000605",
      "district": "13",
      "firstName": "Adam",
      "fullName": "Rep. Gray, Adam [D-CA-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Gray",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "CA"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
      "state": "IA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "NJ"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "NC"
    },
    {
      "bioguideId": "H001093",
      "district": "9",
      "firstName": "Erin",
      "fullName": "Rep. Houchin, Erin [R-IN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Houchin",
      "party": "R",
      "sponsorshipDate": "2026-05-07",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6143ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6143\nIN THE HOUSE OF REPRESENTATIVES\nNovember 19, 2025 Mrs. Hinson (for herself, Mr. Panetta , Mr. Finstad , and Mr. Gray ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo leverage incentives for the adoption of precision agriculture technology, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Producing Responsible Energy and Conservation Incentives and Solutions for the Environment Act or the PRECISE Act .\n#### 2. Conservation loan and loan guarantee program\nSection 304 of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1924 ) is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (3), by redesignating subparagraphs (F) and (G) as subparagraphs (G) and (H), respectively, and inserting after subparagraph (E) the following:\n(F) the adoption of precision agriculture practices, and the acquisition of precision agriculture technology; ; and\n**(B)**\nby adding at the end the following:\n(4) Precision agriculture; precision agriculture technology The terms precision agriculture and precision agriculture technology have the meanings given those terms in section 1201 of the Food Security Act of 1985. ; and\n**(2)**\nin subsection (d)\u2014\n**(A)**\nin paragraph (2), by striking and ;\n**(B)**\nin paragraph (3), by striking the period and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(4) producers who use the loans to adopt precision agriculture practices or acquire precision agriculture technology, including adoption or acquisition for the purpose of participating in the environmental quality incentives program under subchapter A of chapter 4 of subtitle D of title XII of the Food Security Act of 1985. .\n#### 3. Assistance to rural entities\nSection 310B(a) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1932(a) ) is amended\u2014\n**(1)**\nin paragraph (1), by adding at the end the following:\n(C) Precision agriculture; precision agriculture technology The terms precision agriculture and precision agriculture technology have the meanings given those terms in section 1201 of the Food Security Act of 1985. ; and\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nby striking and at the end of subparagraph (C);\n**(B)**\nby striking the period at the end of subparagraph (D) and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(E) expanding the adoption of precision agriculture practices, including by financing the acquisition of precision agriculture technology, in order to promote best practices, reduce costs, and improve the environment. .\n#### 4. Food Security Act of 1985 definitions\nSection 1201(a) of the Food Security Act of 1985 ( 16 U.S.C. 3801(a) ) is amended\u2014\n**(1)**\nby redesignating paragraphs (20) through (27) as paragraphs (22) through (29), respectively; and\n**(2)**\nby inserting after paragraph (19) the following:\n(20) Precision agriculture The term precision agriculture means managing, tracking, or reducing crop or livestock production inputs, including seed, feed, fertilizer, chemicals, water, and time, at a heightened level of spatial and temporal granularity to improve efficiencies, reduce waste, and maintain environmental quality. (21) Precision agriculture technology The term precision agriculture technology means any technology (including equipment that is necessary for the deployment of such technology) that directly contributes to a reduction in, or improved efficiency of, inputs used in crop or livestock production, including\u2014 (A) Global Positioning System-based or geospatial mapping technology; (B) satellite or aerial imagery technology; (C) yield monitors; (D) soil mapping technology; (E) sensors for gathering data on crop, soil, or livestock conditions; (F) Internet of Things and telematics technologies; (G) data management software and advanced analytics; (H) network connectivity products and solutions; (I) Global Positioning System guidance or auto-steer systems; (J) variable rate technology for applying inputs, such as section control; and (K) any other technology, as determined by the Secretary, that directly contributes to a reduction in, or improved efficiency of, crop or livestock production inputs, which may include seed, feed, fertilizer, chemicals, water, and time. .\n#### 5. Environmental Quality Incentives Program\n##### (a) Definitions\nSection 1240A(6)(B)(v) of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u20131(6)(B)(v) ) is amended by inserting (including the adoption of precision agriculture practices and the acquisition of precision agriculture technology) after planning .\n##### (b) Payments\n**(1) Other payments**\nSection 1240B(d)(6) of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u20132(d)(6) ) is amended\u2014\n**(A)**\nby striking A producer shall and inserting the following:\n(A) Payments under this subtitle A producer shall ; and\n**(B)**\nby adding at the end the following:\n(B) Conservation loan and loan guarantee program payments (i) In general A producer receiving payments for practices on eligible land under the program may also receive a loan or loan guarantee under section 304 of the Consolidated Farm and Rural Development Act to cover costs for the same practices on the same land. (ii) Notice to producer The Secretary shall inform a producer participating in the program in writing that such producer may apply for a loan or loan guarantee under section 304 of the Consolidated Farm and Rural Development Act as it relates to costs of implementing practices under this program. .\n**(2) Increased payments for high-priority practices**\nSection 1240B(d)(7) of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u20132(d)(7) ) is amended, in the paragraph heading, by inserting State-determined before high-priority .\n**(3) Increased payments for precision agriculture**\nSection 1240B(d) of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u20132(d) ) is amended by adding at the end the following:\n(8) Increased payments for precision agriculture Notwithstanding paragraph (2), the Secretary may increase the amount that would otherwise be provided for a practice under this subsection to not more than 90 percent of the costs associated with adopting precision agriculture practices and acquiring precision agriculture technology for the purpose of implementing conservation practices. .\n##### (c) Conservation incentive contracts\nSection 1240B(j)(2)(A)(i) of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u20132(j)(3)(A)(i) ) is amended by inserting (which may include the adoption of precision agriculture practices and the acquisition of precision agriculture technology) after incentive practices .\n#### 6. Conservation Stewardship Program\nSection 1240L(d) of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u201324(d) ) is amended\u2014\n**(1)**\nin the subsection heading, by striking and advanced grazing management and inserting , advanced grazing management, and precision agriculture ;\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nin subparagraph (A), by striking ; or and inserting a semicolon;\n**(B)**\nin subparagraph (B), by striking the period at the end and inserting ; or ; and\n**(C)**\nby adding at the end the following:\n(C) precision agriculture conservation activities. ; and\n**(3)**\nin paragraph (3), by striking or advanced grazing management and inserting , advanced grazing management, or precision agriculture conservation activities .\n#### 7. Delivery of technical assistance\nSection 1242(f) of the Food Security Act of 1985 ( 16 U.S.C. 3842(f) ) is amended by adding at the end the following:\n(6) Soil health planning The Secretary shall emphasize the use of third-party providers in providing technical assistance for soil health planning, including planning related to the use of cover crops, precision agriculture practices, comprehensive nutrient management planning, and other innovative plans. .",
      "versionDate": "2025-11-19",
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
        "updateDate": "2025-12-02T20:47:00Z"
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
      "date": "2025-11-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6143ih.xml"
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
      "title": "PRECISE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-29T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PRECISE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-29T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Producing Responsible Energy and Conservation Incentives and Solutions for the Environment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-29T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To leverage incentives for the adoption of precision agriculture technology, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-29T05:18:21Z"
    }
  ]
}
```
