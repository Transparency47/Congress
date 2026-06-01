# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/156?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/156
- Title: Increased TSP Access Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 156
- Origin chamber: Senate
- Introduced date: 2025-01-21
- Update date: 2026-02-05T12:03:16Z
- Update date including text: 2026-02-05T12:03:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-21: Introduced in Senate
- 2025-01-21 - IntroReferral: Introduced in Senate
- 2025-01-21 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-01-21: Introduced in Senate

## Actions

- 2025-01-21 - IntroReferral: Introduced in Senate
- 2025-01-21 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-21",
    "latestAction": {
      "actionDate": "2025-01-21",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/156",
    "number": "156",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "M001198",
        "district": "",
        "firstName": "Roger",
        "fullName": "Sen. Marshall, Roger [R-KS]",
        "lastName": "Marshall",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "Increased TSP Access Act of 2025",
    "type": "S",
    "updateDate": "2026-02-05T12:03:16Z",
    "updateDateIncludingText": "2026-02-05T12:03:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-21",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-21",
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
            "date": "2025-01-21T16:35:09Z",
            "name": "Referred To"
          },
          {
            "date": "2025-01-21T16:35:09Z",
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
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-01-21",
      "state": "CO"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s156is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 156\nIN THE SENATE OF THE UNITED STATES\nJanuary 21, 2025 Mr. Marshall (for himself and Mr. Bennet ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Food Security Act of 1985 to modify the delivery of technical assistance, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Increased TSP Access Act of 2025 .\n#### 2. Delivery of technical assistance\nSection 1242 of the Food Security Act of 1985 ( 16 U.S.C. 3842 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby redesignating paragraph (2) as paragraph (3); and\n**(B)**\nby inserting after paragraph (1) the following:\n(2) Non-Federal certifying entity The term non-Federal certifying entity means a non-Federal entity or State agency described in subparagraph (A) or (B), respectively, of subsection (e)(4). ;\n**(2)**\nin subsection (b), by striking science-based, site-specific practices designed and inserting timely, science-based, and site-specific practice design and implementation assistance ;\n**(3)**\nin subsection (d), by inserting (including private sector entities) after non-Federal entities ;\n**(4)**\nin subsection (e)\u2014\n**(A)**\nin paragraph (2), by striking Food, Conservation, and Energy Act of 2008 and inserting Increased TSP Access Act of 2025 ;\n**(B)**\nin paragraph (3)\u2014\n**(i)**\nin subparagraph (A), by striking ensure and all that follows through engineering, and inserting ensure that third-party providers with expertise in the technical aspects of conservation planning, watershed planning, environmental engineering, conservation practice design, implementation, and evaluation, or other technical skills, as determined by the Secretary, ; and\n**(ii)**\nin subparagraph (C), by inserting by the Secretary after established ; and\n**(C)**\nby striking paragraphs (4) and (5) and inserting the following:\n(4) Certification The Secretary shall certify a third-party provider through\u2014 (A) a certification process administered by the Secretary, acting through the Chief of the Natural Resources Conservation Service; (B) a non-Federal entity (other than a State agency) approved by the Secretary to perform the certification; or (C) a State agency with statutory authority to certify, administer, or license professionals in one or more fields of natural resources, agriculture, or engineering approved by the Secretary to perform the certification. (5) Timely decisions Not later than 10 business days after the date on which the Secretary receives a notification submitted by a non-Federal certifying entity that the non-Federal certifying entity has certified a third-party provider, the Secretary shall\u2014 (A) review the certification; and (B) if the certification is satisfactory to the Secretary, include the name of the third-party provider on the registry of certified third-party providers maintained by the Secretary. (6) Non-Federal certifying entity process (A) Establishment Not later than 180 days after the date of enactment of the Increased TSP Access Act of 2025 , the Secretary shall establish a process for the certification of third-party providers by non-Federal certifying entities, with the goal of increasing third-party provider capacity, including the certification of qualified agricultural retailers, cooperatives, professional societies, service providers, and organizations described in section 1265A(3)(B)(i). (B) Eligibility of non-Federal certifying entities In determining the eligibility of a non-Federal certifying entity under subparagraph (A), the Secretary shall consider\u2014 (i) the ability of the non-Federal certifying entity to assess qualifications of a third-party provider and certify third-party providers at scale; (ii) the experience of the non-Federal certifying entity in working with third-party providers and eligible participants; (iii) the expertise of the non-Federal certifying entity in the technical and science-based aspects of conservation delivery described in paragraph (3)(A); (iv) the history of the non-Federal certifying entity in working with agricultural producers; and (v) such other qualifications as the Secretary determines to be appropriate. (C) Approval Not later than 40 business days after the date on which the Secretary receives an application submitted by a non-Federal certifying entity to certify third-party providers under this section, the Secretary shall make a decision on whether to approve the non-Federal certifying entity to certify third-party providers. (D) Duties of non-Federal certifying entities A non-Federal certifying entity approved by the Secretary to certify third-party providers shall\u2014 (i) assess the ability of a third-party provider to appropriately provide technical assistance to eligible participants; (ii) provide training to ensure that a third-party provider certified by the non-Federal certifying entity is qualified to provide that technical assistance; and (iii) submit to the Secretary a timely notice of\u2014 (I) each third-party provider certified by the non-Federal certifying entity, for inclusion on the registry of certified third-party providers maintained by the Secretary; and (II) each third-party provider the certification of which is withdrawn by the non-Federal certifying entity. (7) Streamlined certification Not later than 180 days after the date of enactment of the Increased TSP Access Act of 2025 , the Secretary shall provide a streamlined certification process for a third-party provider that has an appropriate specialty certification, including a certified crop advisor certified by the American Society of Agronomy, a professional engineer, or a holder of a technical certification approved by the Secretary. ; and\n**(5)**\nin subsection (f)\u2014\n**(A)**\nin paragraph (2), in the matter preceding subparagraph (A), by inserting or a non-Federal certifying entity after third-party provider ;\n**(B)**\nby striking paragraph (3) and inserting the following:\n(3) Review Not later than 1 year after the date of enactment of the Increased TSP Access Act of 2025 , and additionally thereafter at the discretion of the Secretary, the Secretary shall\u2014 (A) review certification requirements for third-party providers; (B) make any adjustments considered necessary by the Secretary to improve participation and the quality and effectiveness of conservation practices implemented and adopted with support from technical service providers; (C) conduct outreach to and receive input from third-party providers, both that currently participate in the program under this section and those that no longer participate in the program, and entities, organizations, and associations providing or supporting consultative services to agriculture, livestock, and forest producers to assess barriers and opportunities for the use of third-party provider assistance for improved conservation program delivery; and (D) set a target utilization rate for third-party providers. ;\n**(C)**\nin paragraph (4)(A)(i), by inserting maintenance, after outreach, ; and\n**(D)**\nby striking paragraph (5) and inserting the following:\n(5) Payment amounts (A) In general The Secretary shall establish fair and reasonable amounts of payments for technical services provided by third-party providers at rates equivalent to, but that do not exceed, technical assistance provided by the Secretary. (B) Considerations In determining fair and reasonable payment amounts under subparagraph (A), the Secretary shall consider specialized equipment, frequency of site visits, training, travel and transportation, and such other factors as the Secretary determines to be appropriate. (C) Exclusion A payment provided under another Federal program directly to an eligible participant for technical assistance provided by a third-party provider certified under this section shall be\u2014 (i) excluded from cost-sharing requirements under the program under which the payment was provided; and (ii) equal to not more than 100 percent of the fair and reasonable payment amount for the applicable technical assistance determined under subparagraph (B). (6) Transparency Not later than 1 year after the date of enactment of the Increased TSP Access Act of 2025 , the Secretary shall provide accessible public information on\u2014 (A) funds obligated to third-party providers through\u2014 (i) contracts entered into between eligible participants and individual third-party providers; and (ii) agreements with public and private sector entities to secure third-party technical assistance; (B) certification results, including\u2014 (i) the number of third-party providers certified by the Secretary; (ii) the number of non-Federal certifying entities approved by the Secretary; (iii) the number of third-party providers certified by non-Federal certifying entities; and (iv) the number of third-party providers certified based on State agency or professional association credentialing; (C) how third-party providers contribute to the quality and effectiveness of conservation practices implemented and adopted, and what improvements are needed; and (D) the target utilization rate set under paragraph (3)(D) and how actual utilization compares to that target rate. .",
      "versionDate": "2025-01-21",
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
        "actionDate": "2025-02-28",
        "text": "Referred to the Subcommittee on Conservation, Research, and Biotechnology."
      },
      "number": "575",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Increased TSP Access Act of 2025",
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
        "updateDate": "2025-02-25T15:08:52Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-21",
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
          "measure-id": "id119s156",
          "measure-number": "156",
          "measure-type": "s",
          "orig-publish-date": "2025-01-21",
          "originChamber": "SENATE",
          "update-date": "2025-03-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s156v00",
            "update-date": "2025-03-17"
          },
          "action-date": "2025-01-21",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Increased TSP Access Act of 2025</strong></p><p>This bill directs the Department of Agriculture (USDA) to modify the\u00a0certification process for Technical Service Providers (TSPs) at the Natural Resources Conservation Service (NRCS) by establishing an approval process for nonfederal certifying entities and a streamlined certification process for TSPs that hold certain specialty certifications.</p><p>As background, TSPs are third-party service providers, such as private businesses, Indian tribes, and nonprofit organizations, that work on behalf of customers to offer planning, design, and implementation services that meet NRCS criteria.</p><p>The bill specifies that USDA must ensure, to the maximum extent practicable, third-party providers with expertise in the technical aspects of conservation practice design, implementation, and evaluation are eligible to become approved TSPs.</p><p>USDA must provide a streamlined certification process for TSPs who hold appropriate specialty certifications (e.g., certified crop advisors).</p><p>In determining the eligibility of a nonfederal certifying entity, USDA must consider the ability, experience, expertise, and history of the entity. USDA must decide whether to approve an application submitted by a nonfederal certifying entity to certify\u00a0TSPs\u00a0within a specified time period. \u00a0</p><p>USDA must also review a TSP's certification by a nonfederal certifying entity within a specified time period. If the certification is satisfactory, USDA must include the\u00a0TSP on a USDA-maintained registry of certified TSPs.</p><p>The bill also specifies that TSPs must be paid at rates equivalent to technical assistance provided by USDA.</p><p>Further, USDA must provide accessible public information on TSPs, including information on funding, certification results, and utilization rates.</p>"
        },
        "title": "Increased TSP Access Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s156.xml",
    "summary": {
      "actionDate": "2025-01-21",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Increased TSP Access Act of 2025</strong></p><p>This bill directs the Department of Agriculture (USDA) to modify the\u00a0certification process for Technical Service Providers (TSPs) at the Natural Resources Conservation Service (NRCS) by establishing an approval process for nonfederal certifying entities and a streamlined certification process for TSPs that hold certain specialty certifications.</p><p>As background, TSPs are third-party service providers, such as private businesses, Indian tribes, and nonprofit organizations, that work on behalf of customers to offer planning, design, and implementation services that meet NRCS criteria.</p><p>The bill specifies that USDA must ensure, to the maximum extent practicable, third-party providers with expertise in the technical aspects of conservation practice design, implementation, and evaluation are eligible to become approved TSPs.</p><p>USDA must provide a streamlined certification process for TSPs who hold appropriate specialty certifications (e.g., certified crop advisors).</p><p>In determining the eligibility of a nonfederal certifying entity, USDA must consider the ability, experience, expertise, and history of the entity. USDA must decide whether to approve an application submitted by a nonfederal certifying entity to certify\u00a0TSPs\u00a0within a specified time period. \u00a0</p><p>USDA must also review a TSP's certification by a nonfederal certifying entity within a specified time period. If the certification is satisfactory, USDA must include the\u00a0TSP on a USDA-maintained registry of certified TSPs.</p><p>The bill also specifies that TSPs must be paid at rates equivalent to technical assistance provided by USDA.</p><p>Further, USDA must provide accessible public information on TSPs, including information on funding, certification results, and utilization rates.</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119s156"
    },
    "title": "Increased TSP Access Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-21",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Increased TSP Access Act of 2025</strong></p><p>This bill directs the Department of Agriculture (USDA) to modify the\u00a0certification process for Technical Service Providers (TSPs) at the Natural Resources Conservation Service (NRCS) by establishing an approval process for nonfederal certifying entities and a streamlined certification process for TSPs that hold certain specialty certifications.</p><p>As background, TSPs are third-party service providers, such as private businesses, Indian tribes, and nonprofit organizations, that work on behalf of customers to offer planning, design, and implementation services that meet NRCS criteria.</p><p>The bill specifies that USDA must ensure, to the maximum extent practicable, third-party providers with expertise in the technical aspects of conservation practice design, implementation, and evaluation are eligible to become approved TSPs.</p><p>USDA must provide a streamlined certification process for TSPs who hold appropriate specialty certifications (e.g., certified crop advisors).</p><p>In determining the eligibility of a nonfederal certifying entity, USDA must consider the ability, experience, expertise, and history of the entity. USDA must decide whether to approve an application submitted by a nonfederal certifying entity to certify\u00a0TSPs\u00a0within a specified time period. \u00a0</p><p>USDA must also review a TSP's certification by a nonfederal certifying entity within a specified time period. If the certification is satisfactory, USDA must include the\u00a0TSP on a USDA-maintained registry of certified TSPs.</p><p>The bill also specifies that TSPs must be paid at rates equivalent to technical assistance provided by USDA.</p><p>Further, USDA must provide accessible public information on TSPs, including information on funding, certification results, and utilization rates.</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119s156"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s156is.xml"
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
      "title": "Increased TSP Access Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-05T12:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Increased TSP Access Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-21T03:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Food Security Act of 1985 to modify the delivery of technical assistance, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-21T03:33:27Z"
    }
  ]
}
```
