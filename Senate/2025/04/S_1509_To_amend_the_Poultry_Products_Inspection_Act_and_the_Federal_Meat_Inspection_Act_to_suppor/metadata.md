# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1509?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1509
- Title: Strengthening Local Processing Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1509
- Origin chamber: Senate
- Introduced date: 2025-04-29
- Update date: 2026-02-10T12:03:17Z
- Update date including text: 2026-02-10T12:03:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-29: Introduced in Senate
- 2025-04-29 - IntroReferral: Introduced in Senate
- 2025-04-29 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (text: CR S2666-2668)
- Latest action: 2025-04-29: Introduced in Senate

## Actions

- 2025-04-29 - IntroReferral: Introduced in Senate
- 2025-04-29 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (text: CR S2666-2668)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-29",
    "latestAction": {
      "actionDate": "2025-04-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1509",
    "number": "1509",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "T000250",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Thune, John [R-SD]",
        "lastName": "Thune",
        "party": "R",
        "state": "SD"
      }
    ],
    "title": "Strengthening Local Processing Act of 2025",
    "type": "S",
    "updateDate": "2026-02-10T12:03:17Z",
    "updateDateIncludingText": "2026-02-10T12:03:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-29",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (text: CR S2666-2668)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-29",
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
        "item": [
          {
            "date": "2025-04-29T18:39:59Z",
            "name": "Referred To"
          },
          {
            "date": "2025-04-29T18:39:59Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "MN"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1509is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1509\nIN THE SENATE OF THE UNITED STATES\nApril 29, 2025 Mr. Thune (for himself and Ms. Smith ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Poultry Products Inspection Act and the Federal Meat Inspection Act to support small and very small meat and poultry processing establishments, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Strengthening Local Processing Act of 2025 .\n#### 2. HACCP guidance and resources for smaller and very small poultry and meat establishments\n##### (a) Poultry establishments\nThe Poultry Products Inspection Act is amended by inserting after section 14 ( 21 U.S.C. 463 ) the following:\n14A. Smaller and very small establishment guidance and resources (a) Definitions of smaller establishment and very small establishment In this section, the terms smaller establishment and very small establishment have the meanings given those terms in the final rule entitled \u2018Pathogen Reduction; Hazard Analysis and Critical Control Point (HACCP) Systems\u2019 (61 Fed. Reg. 38806 (July 25, 1996)). (b) Database of studies; model plans Not later than 18 months after the date of enactment of this section, the Secretary shall\u2014 (1) establish a free, searchable database of approved peer-reviewed validation studies accessible to smaller establishments and very small establishments subject to inspection under this Act for use in developing a Hazard Analysis and Critical Control Points plan; and (2) publish online scale-appropriate model Hazard Analysis and Critical Control Points plans for smaller establishments and very small establishments, including model plans for\u2014 (A) slaughter-only establishments; (B) processing-only establishments; and (C) slaughter and processing establishments. (c) Guidance Not later than 2 years after the date of enactment of this section, the Secretary shall publish a guidance document, after notice and an opportunity for public comment, providing information on the requirements that need to be met for smaller establishments and very small establishments to receive approval for a Hazard Analysis and Critical Control Points plan pursuant to this Act. (d) Data confidentiality In carrying out subsections (b) and (c), the Secretary shall not publish confidential business information, including a Hazard Analysis and Critical Control Points plan of an establishment. .\n##### (b) Meat establishments\nThe Federal Meat Inspection Act is amended by inserting after section 25 ( 21 U.S.C. 625 ) the following:\n26. Smaller and very small establishment guidance and resources (a) Definitions of smaller establishment and very small establishment In this section, the terms smaller establishment and very small establishment have the meanings given those terms in the final rule entitled \u2018Pathogen Reduction; Hazard Analysis and Critical Control Point (HACCP) Systems\u2019 (61 Fed. Reg. 38806 (July 25, 1996)). (b) Database of studies; model plans Not later than 18 months after the date of enactment of this section, the Secretary shall\u2014 (1) establish a free, searchable database of approved peer-reviewed validation studies accessible to smaller establishments and very small establishments subject to inspection under this Act for use in developing a Hazard Analysis and Critical Control Points plan; and (2) publish online scale-appropriate model Hazard Analysis and Critical Control Points plans for smaller establishments and very small establishments, including model plans for\u2014 (A) slaughter-only establishments; (B) processing-only establishments; and (C) slaughter and processing establishments. (c) Guidance Not later than 2 years after the date of enactment of this section, the Secretary shall publish a guidance document, after notice and an opportunity for public comment, providing information on the requirements that need to be met for smaller establishments and very small establishments to receive approval for a Hazard Analysis and Critical Control Points plan pursuant to this Act. (d) Data confidentiality In carrying out subsections (b) and (c), the Secretary shall not publish confidential business information, including a Hazard Analysis and Critical Control Points plan of an establishment. .\n#### 3. Increasing maximum Federal share for expenses of State inspection\n##### (a) Poultry products\nSection 5(a)(3) of the Poultry Products Inspection Act ( 21 U.S.C. 454(a)(3) ) is amended in the second sentence by striking 50 per centum and inserting 65 percent .\n##### (b) Meat and meat food products\nSection 301(a)(3) of the Federal Meat Inspection Act ( 21 U.S.C. 661(a)(3) ) is amended in the second sentence by striking 50 per centum and inserting 65 percent .\n#### 4. Cooperative interstate shipment of poultry and meat\n##### (a) Poultry products\nSection 31 of the Poultry Products Inspection Act ( 21 U.S.C. 472 ) is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (2), by striking 25 employees each place it appears and inserting 50 employees ; and\n**(B)**\nin paragraph (3)\u2014\n**(i)**\nin the paragraph heading, by striking 25 and inserting 50 ;\n**(ii)**\nin subparagraph (A), by striking 25 and inserting 50 ; and\n**(iii)**\nin subparagraph (B)\u2014\n**(I)**\nin clause (i), by striking more than 25 employees but less than 35 employees and inserting more than 50 employees but less than 70 employees ; and\n**(II)**\nin clause (ii), by striking subsection (i) and inserting subsection (j) ;\n**(2)**\nin subsection (c), by striking 60 percent and inserting 80 percent ;\n**(3)**\nin subsection (e)(1), by striking subsection (i) and inserting subsection (j) ;\n**(4)**\nby redesignating subsections (f) through (i) as subsections (g) through (j), respectively; and\n**(5)**\nby inserting after subsection (e) the following:\n(f) Federal outreach (1) In general In each of fiscal years 2025 through 2030, for the purpose of State participation in the Cooperative Interstate Shipment program, the Secretary shall conduct outreach to, and, as appropriate, subsequent negotiation with, not fewer than 25 percent of the States that\u2014 (A) have a State poultry product inspection program pursuant to section 5; but (B) do not have a selected establishment. (2) Report At the conclusion of each of fiscal years 2025 through 2030, the Secretary shall submit a report detailing the activities and results of the outreach conducted during that fiscal year under paragraph (1) to\u2014 (A) the Committee on Agriculture of the House of Representatives; (B) the Committee on Agriculture, Nutrition, and Forestry of the Senate; (C) the Subcommittee on Agriculture, Rural Development, Food and Drug Administration, and Related Agencies of the Committee on Appropriations of the House of Representatives; and (D) the Subcommittee on Agriculture, Rural Development, Food and Drug Administration, and Related Agencies of the Committee on Appropriations of the Senate. .\n##### (b) Meat and meat food products\nSection 501 of the Federal Meat Inspection Act ( 21 U.S.C. 683 ) is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (2), by striking 25 employees each place it appears and inserting 50 employees ; and\n**(B)**\nin paragraph (3)\u2014\n**(i)**\nin the paragraph heading, by striking 25 and inserting 50 ;\n**(ii)**\nin subparagraph (A), by striking 25 and inserting 50 ; and\n**(iii)**\nin subparagraph (B)(i), by striking more than 25 employees but less than 35 employees and inserting more than 50 employees but less than 70 employees ;\n**(2)**\nin subsection (c), by striking 60 percent and inserting 80 percent ; and\n**(3)**\nin subsection (f), by adding at the end the following:\n(3) Federal outreach (A) In general In each of fiscal years 2025 through 2030, for the purpose of State participation in the Cooperative Interstate Shipment program, the Secretary shall conduct outreach to, and, as appropriate, subsequent negotiation with, not fewer than 25 percent of the States that\u2014 (i) have a State meat inspection program pursuant to section 301; but (ii) do not have a selected establishment. (B) Report At the conclusion of each of fiscal years 2025 through 2030, the Secretary shall submit a report detailing the activities and results of the outreach conducted during that fiscal year under subparagraph (A) to\u2014 (i) the Committee on Agriculture of the House of Representatives; (ii) the Committee on Agriculture, Nutrition, and Forestry of the Senate; (iii) the Subcommittee on Agriculture, Rural Development, Food and Drug Administration, and Related Agencies of the Committee on Appropriations of the House of Representatives; and (iv) the Subcommittee on Agriculture, Rural Development, Food and Drug Administration, and Related Agencies of the Committee on Appropriations of the Senate. .\n#### 5. Processing resilience grant program\nSubtitle A of the Agricultural Marketing Act of 1946 ( 7 U.S.C. 1621 et seq. ) is amended by adding at the end the following:\n210B. Processing resilience grant program (a) Definitions In this section: (1) Eligible entity The term eligible entity means\u2014 (A) a smaller establishment or very small establishment (as those terms are defined in the final rule entitled \u2018Pathogen Reduction; Hazard Analysis and Critical Control Point (HACCP) Systems\u2019 (61 Fed. Reg. 33806 (July 25, 1996))); (B) a slaughtering or processing establishment subject to\u2014 (i) a State meat inspection program pursuant to section 301 of the Federal Meat Inspection Act ( 21 U.S.C. 661 ); or (ii) a State poultry product inspection program pursuant to section 5 of the Poultry Products Inspection Act ( 21 U.S.C. 454 ); (C) a person engaging in custom operations that is exempt from inspection under\u2014 (i) section 23 of the Federal Meat Inspection Act ( 21 U.S.C. 623 ); or (ii) section 15 of the Poultry Products Inspection Act ( 21 U.S.C. 464 ); and (D) a person seeking\u2014 (i) to establish and operate an establishment described in subparagraph (A) or (B); or (ii) to engage in custom operations described in subparagraph (C). (2) Secretary The term Secretary means the Secretary of Agriculture, acting through the Administrator of the Agricultural Marketing Service. (b) Grants (1) In general Not later than 60 days after the date of enactment of this section, the Secretary shall award competitive grants to eligible entities for activities to increase resiliency and diversification of the meat processing system, including activities that\u2014 (A) support the health and safety of meat and poultry plant employees, suppliers, and customers; (B) support increased processing capacity; and (C) otherwise support the resilience of the small meat and poultry processing sector. (2) Maximum amount The maximum amount of a grant awarded under this section shall not exceed $500,000. (3) Duration The term of a grant awarded under this section shall not exceed 3 years. (c) Applications (1) In general An eligible entity desiring a grant under this section shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require. (2) Applications for small grants The Secretary shall establish a separate, simplified application process for eligible entities applying for a grant under this section of not more than $100,000. (3) Requirements The Secretary shall ensure that any application for a grant under this section is\u2014 (A) simple and practicable; (B) accessible online; and (C) available through local staff of the Department of Agriculture. (4) Notice Not later than 14 days before the date on which the Secretary begins to accept applications under paragraph (1), the Secretary shall publish a notice of funding opportunity with respect to the grants available under this section. (5) Reapplication If an application of an eligible entity under this subsection is denied by the Secretary, the eligible entity may submit a revised application. (6) Priority In reviewing applications submitted under this subsection, the Secretary shall give priority to proposals that will\u2014 (A) increase farmer and rancher access to animal slaughter options within a 200-mile radius of the location of the farmer or rancher; or (B) support an eligible entity described in subsection (a)(1)(A). (d) Use of grant An eligible entity that receives a grant under this section shall use the grant funds to carry out activities in support of the purposes described in subsection (b)(1), including through\u2014 (1) the development and issuance of a Hazard Analysis and Critical Control Points plan for the eligible entity, which may be developed by a consultant; (2) the purchase or establishment, as applicable, of facilities, equipment, processes, and operations necessary for the eligible entity to comply with applicable requirements under the Federal Meat Inspection Act ( 21 U.S.C. 601 et seq. ) or the Poultry Products Inspection Act ( 21 U.S.C. 451 et seq. ); (3) the purchase of cold storage, equipment, or transportation services; (4) the purchase of temperature screening supplies, testing for communicable diseases, disinfectant, sanitation systems, hand washing stations, and other sanitizing supplies; (5) the purchase and decontamination of personal protective equipment; (6) the construction or purchase of humane handling infrastructure, including holding space for livestock prior to slaughter, shade structures, and knock box structures; (7) (A) the purchase of software and computer equipment for record keeping, production data, and Hazard Analysis and Critical Control Points record review; and (B) the provision of guidelines and training relating to that software and computer equipment; (8) the provision of staff time and training for implementing and monitoring health and safety procedures; (9) the development of a feasibility study or business plan for, or the carrying out of any other activity associated with, establishing or expanding a small meat or poultry processing facility; (10) the purchase of equipment that enables the further use or value-added sale of coproducts or byproducts, such as organs, hides, and other relevant products; and (11) other activities associated with expanding or establishing an eligible entity described in subsection (a)(1)(A), as determined by the Secretary. (e) Outreach During the period beginning on the date on which the Secretary publishes the notice under subsection (c)(4) and ending on the date on which the Secretary begins to accept applications under subsection (c)(1), the Secretary shall perform outreach to States and eligible entities relating to grants under this section. (f) Federal share (1) In general Subject to paragraph (2), the Federal share of the activities carried out using a grant awarded under this section shall not exceed\u2014 (A) 90 percent in the case of a grant in the amount of $100,000 or less; or (B) 75 percent in the case of a grant in an amount greater than $100,000. (2) Fiscal years 2025 and 2026 An eligible entity awarded a grant under this section during fiscal year 2025 or 2026 shall not be required to provide non-Federal matching funds with respect to the grant. (g) Administration The promulgation of regulations under, and administration of, this section shall be made without regard to\u2014 (1) the notice and comment provisions of section 553 of title 5, United States Code; and (2) chapter 35 of title 44, United States Code (commonly known as the Paperwork Reduction Act ). (h) Authorization of appropriations There is authorized to be appropriated to the Secretary of Agriculture to carry out this section $20,000,000 for each of fiscal years 2025 through 2030. .\n#### 6. Processor career training programs\nTitle IV of the Agricultural Research, Extension, and Education Reform Act of 1998 is amended by inserting before section 404 ( 7 U.S.C. 7624 ) the following:\n403. Processor career training programs (a) Definitions In this section: (1) Land-grant colleges and universities The term land-grant colleges and universities has the meaning given the term in section 1404 of the National Agricultural Research, Extension, and Teaching Policy Act of 1977 ( 7 U.S.C. 3103 ). (2) Smaller establishment; very small establishment The terms smaller establishment and very small establishment have the meanings given those terms in the final rule entitled \u2018Pathogen Reduction; Hazard Analysis and Critical Control Point (HACCP) Systems\u2019 (61 Fed. Reg. 38806 (July 25, 1996)). (3) Structured apprenticeship The term structured apprenticeship means an apprenticeship program that\u2014 (A) provides most of the training on the job in a meat or poultry processing facility; (B) describes in detail\u2014 (i) all of the competencies necessary to work in a meat or poultry processing facility; and (ii) the competencies that are necessary to own and operate a meat or poultry processing facility that is a smaller establishment or a very small establishment; (C) describes the level of knowledge, skill, and ability the apprentice ought to attain in each competency; (D) includes a component for someone other than the trainer\u2014 (i) to assess competency attainment; and (ii) to assure that all competencies are being addressed during the apprenticeship; (E) includes an individualized plan for each apprentice that\u2014 (i) considers prior knowledge, skill, and ability; and (ii) allows for apprentices to opt out of competencies irrelevant to their career goals; and (F) focuses on individuals who will work in or operate meat or poultry processing facilities that are smaller establishments or very small establishments. (b) Processor career training programs (1) In general The Secretary shall provide competitive grants to junior or community colleges, technical or vocational schools, nonprofit organizations, worker training centers, and land-grant colleges and universities to establish or expand career training programs, including for structured apprenticeships, relating to meat and poultry processing. (2) Applications for small grants The Secretary shall establish a separate, simplified application and reporting process for entities described in paragraph (1) applying for a grant under this subsection of not more than $100,000. (3) Authorization of appropriations There is authorized to be appropriated to the Secretary to carry out this subsection $10,000,000 for each of fiscal years 2025 through 2030. .",
      "versionDate": "2025-04-29",
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
        "actionDate": "2025-04-29",
        "text": "Referred to the House Committee on Agriculture."
      },
      "number": "3076",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Strengthening Local Processing Act of 2025",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-05-28T15:05:56Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-29",
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
          "measure-id": "id119s1509",
          "measure-number": "1509",
          "measure-type": "s",
          "orig-publish-date": "2025-04-29",
          "originChamber": "SENATE",
          "update-date": "2026-01-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1509v00",
            "update-date": "2026-01-26"
          },
          "action-date": "2025-04-29",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Strengthening Local Processing Act of 2025</strong></p><p>This bill revises provisions related to meat and poultry processing establishments, including by establishing grants and a database\u00a0to assist smaller establishments (i.e., at least 10 but fewer than 500 employees) and very small establishments (i.e., fewer than 10 employees or annual sales of less than $2.5 million).</p><p>For example, the Department of Agriculture (USDA) must establish a searchable database of peer-reviewed validation studies for use in developing Hazard Analysis and Critical Control Points plans for smaller and very small establishments.</p><p>The bill increases the maximum federal cost shares for (1) state meat and poultry inspection programs (from 50% to 65%), and (2) the Cooperative Interstate Shipment (CIS) program (from 60% to 80%).\u00a0The CIS program allows state-inspected facilities to operate as federally-inspected facilities and ship their products in interstate commerce and internationally.</p><p>Additionally, USDA must conduct outreach to states that have meat and poultry inspection programs, but do not participate in the CIS program. The bill also allows certain establishments with up to 50 employees (currently up to 25 employees) to participate in the program.\u00a0</p><p>USDA must also award grants to increase resiliency and diversification of the meat processing system, including activities that support (1) the health and safety of meat and poultry plant employees, suppliers, and customers; (2) increased processing capacity; and (3) the resilience of the small meat and poultry processing sector.</p><p>Further, the bill establishes a grant program for meat and poultry processing career training programs,\u00a0including structured apprenticeships. </p>"
        },
        "title": "Strengthening Local Processing Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1509.xml",
    "summary": {
      "actionDate": "2025-04-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Strengthening Local Processing Act of 2025</strong></p><p>This bill revises provisions related to meat and poultry processing establishments, including by establishing grants and a database\u00a0to assist smaller establishments (i.e., at least 10 but fewer than 500 employees) and very small establishments (i.e., fewer than 10 employees or annual sales of less than $2.5 million).</p><p>For example, the Department of Agriculture (USDA) must establish a searchable database of peer-reviewed validation studies for use in developing Hazard Analysis and Critical Control Points plans for smaller and very small establishments.</p><p>The bill increases the maximum federal cost shares for (1) state meat and poultry inspection programs (from 50% to 65%), and (2) the Cooperative Interstate Shipment (CIS) program (from 60% to 80%).\u00a0The CIS program allows state-inspected facilities to operate as federally-inspected facilities and ship their products in interstate commerce and internationally.</p><p>Additionally, USDA must conduct outreach to states that have meat and poultry inspection programs, but do not participate in the CIS program. The bill also allows certain establishments with up to 50 employees (currently up to 25 employees) to participate in the program.\u00a0</p><p>USDA must also award grants to increase resiliency and diversification of the meat processing system, including activities that support (1) the health and safety of meat and poultry plant employees, suppliers, and customers; (2) increased processing capacity; and (3) the resilience of the small meat and poultry processing sector.</p><p>Further, the bill establishes a grant program for meat and poultry processing career training programs,\u00a0including structured apprenticeships. </p>",
      "updateDate": "2026-01-26",
      "versionCode": "id119s1509"
    },
    "title": "Strengthening Local Processing Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Strengthening Local Processing Act of 2025</strong></p><p>This bill revises provisions related to meat and poultry processing establishments, including by establishing grants and a database\u00a0to assist smaller establishments (i.e., at least 10 but fewer than 500 employees) and very small establishments (i.e., fewer than 10 employees or annual sales of less than $2.5 million).</p><p>For example, the Department of Agriculture (USDA) must establish a searchable database of peer-reviewed validation studies for use in developing Hazard Analysis and Critical Control Points plans for smaller and very small establishments.</p><p>The bill increases the maximum federal cost shares for (1) state meat and poultry inspection programs (from 50% to 65%), and (2) the Cooperative Interstate Shipment (CIS) program (from 60% to 80%).\u00a0The CIS program allows state-inspected facilities to operate as federally-inspected facilities and ship their products in interstate commerce and internationally.</p><p>Additionally, USDA must conduct outreach to states that have meat and poultry inspection programs, but do not participate in the CIS program. The bill also allows certain establishments with up to 50 employees (currently up to 25 employees) to participate in the program.\u00a0</p><p>USDA must also award grants to increase resiliency and diversification of the meat processing system, including activities that support (1) the health and safety of meat and poultry plant employees, suppliers, and customers; (2) increased processing capacity; and (3) the resilience of the small meat and poultry processing sector.</p><p>Further, the bill establishes a grant program for meat and poultry processing career training programs,\u00a0including structured apprenticeships. </p>",
      "updateDate": "2026-01-26",
      "versionCode": "id119s1509"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1509is.xml"
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
      "title": "Strengthening Local Processing Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-10T12:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Strengthening Local Processing Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-09T04:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Poultry Products Inspection Act and the Federal Meat Inspection Act to support small and very small meat and poultry processing establishments, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-09T03:48:22Z"
    }
  ]
}
```
