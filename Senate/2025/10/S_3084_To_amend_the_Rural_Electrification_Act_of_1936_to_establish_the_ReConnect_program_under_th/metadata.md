# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3084?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3084
- Title: ReConnecting Rural America Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3084
- Origin chamber: Senate
- Introduced date: 2025-10-30
- Update date: 2025-12-05T22:00:44Z
- Update date including text: 2025-12-05T22:00:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-10-30: Introduced in Senate
- 2025-10-30 - IntroReferral: Introduced in Senate
- 2025-10-30 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-10-30: Introduced in Senate

## Actions

- 2025-10-30 - IntroReferral: Introduced in Senate
- 2025-10-30 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-30",
    "latestAction": {
      "actionDate": "2025-10-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3084",
    "number": "3084",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
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
    "title": "ReConnecting Rural America Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T22:00:44Z",
    "updateDateIncludingText": "2025-12-05T22:00:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-30",
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
      "actionDate": "2025-10-30",
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
          "date": "2025-10-30T18:00:12Z",
          "name": "Referred To"
        }
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
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-10-30",
      "state": "VT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3084is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3084\nIN THE SENATE OF THE UNITED STATES\nOctober 30, 2025 Mr. Marshall (for himself and Mr. Welch ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Rural Electrification Act of 1936 to establish the ReConnect program under that Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the ReConnecting Rural America Act of 2025 .\n#### 2. Access to broadband telecommunications services in rural areas\n##### (a) In general\nSection 601 of the Rural Electrification Act of 1936 ( 7 U.S.C. 950bb ) is amended\u2014\n**(1)**\nby striking subsections (a) through (f) and inserting the following:\n(a) Purpose The purpose of this section is to provide assistance in the form of grants, loans, and combinations of grants and loans for the costs of the construction, improvement, and acquisition of facilities and equipment for broadband service in rural areas. (b) Definitions In this section: (1) Broadband service The term broadband service means any technology identified by the Secretary as having the capacity to transmit data to enable a subscriber to the service to originate and receive high-quality voice, data, graphics, and video. (2) Rural area (A) In general The term rural area means any area other than\u2014 (i) an area described in clause (i) or (ii) of section 343(a)(13)(A) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1991(a)(13)(A) ); and (ii) a city, town, or incorporated area that has a population of greater than 20,000 inhabitants. (B) Urban area growth The Secretary may, by regulation only, consider an area described in section 343(a)(13)(F)(i)(I) of that Act to not be a rural area for purposes of this section. (C) Exclusion of certain populations The term rural area does not include any population described in subparagraph (H) or (I) of section 343(a)(13) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1991(a)(13) ). (c) Grants, loans, and combinations (1) In general The Secretary shall make grants, loans, and combinations of grants and loans to eligible entities described in subsection (d) to provide funds for the construction, improvement, or acquisition of facilities and equipment for the provision of broadband service in rural areas. (2) Project eligibility To be eligible for a grant, loan, or grant and loan combination under paragraph (1), in addition to the requirements of subsection (d), the project that is the subject of the grant, loan, or grant and loan combination shall\u2014 (A) provide broadband service of at least\u2014 (i) a 100-Mbps downstream transmission capacity; and (ii) a 100-Mbps upstream transmission capacity; and (B) subject to paragraph (4), be carried out in a proposed service territory in which at least 75 percent of the households lack access to broadband service of at least\u2014 (i) a 100-Mbps downstream transmission capacity; and (ii) a 20-Mbps upstream transmission capacity. (3) Priority In making grants, loans, and grant and loan combinations under paragraph (1), the Secretary\u2014 (A) shall give priority to applications for projects to provide broadband service in a proposed service territory in which at least 90 percent of households lack access to broadband service of at least\u2014 (i) a 100-Mbps downstream transmission capacity; and (ii) a 20-Mbps upstream transmission capacity; and (B) may give priority to applications for projects to provide broadband service\u2014 (i) in proposed service territories\u2014 (I) with a population of less than 10,000 permanent residents; (II) that are experiencing outmigration and have adopted a strategic community investment plan under section 379H(d) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 2008v(d) ) that includes considerations for improving and expanding broadband service; (III) with a high percentage of low-income families or persons (as defined in section 501(b) of the Housing Act of 1949 ( 42 U.S.C. 1471(b) )); or (IV) that are isolated from other significant population centers; (ii) that would provide rapid and expanded deployment of fixed and mobile broadband service on cropland and ranchland within the service territory for use in various applications of precision agriculture; or (iii) submitted by an eligible entity that has provided broadband service or other utility service for not less than 5 years in rural areas in the State in which the project would be carried out. (4) Additional requirements for grant-only awards To be eligible for assistance under paragraph (1) in the form of a grant only, in addition to the requirements of subsection (d)\u2014 (A) an entity shall be\u2014 (i) a Tribal organization (as defined in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 )); (ii) a colonia; (iii) a persistent poverty county, as determined by the Secretary; or (iv) a socially vulnerable community, as determined by the Secretary; or (B) the project that is the subject of the grant shall be carried out in a proposed service territory in which at least 90 percent of households lack access to broadband service of at least\u2014 (i) a 100-Mbps downstream transmission capacity; and (ii) a 20-Mbps upstream transmission capacity. (d) Eligibility (1) Eligible entities (A) In general To be eligible to obtain a grant, loan, or grant and loan combination under subsection (c), an entity shall\u2014 (i) submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require; (ii) agree to complete buildout of the broadband infrastructure described in the application by not later than 5 years after the initial date on which assistance under subsection (c) is made available; and (iii) participate or agree to participate in\u2014 (I) the Lifeline program under subpart E of part 54 of title 47, Code of Federal Regulations (or any successor regulation); or (II) any successor Federal internet affordability assistance program. (B) Inclusions An entity eligible to obtain a grant, loan, or grant and loan combination under subsection (c) may include\u2014 (i) a State or local government, including any agency, subdivision, instrumentality, or political subdivision of a State or local government; (ii) a territory or possession of the United States; (iii) an Indian Tribe (as defined in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 )); (iv) a cooperative or mutual organization; (v) an organization of 2 or more incorporated areas that have established an intermunicipal legal agreement for the purpose of delivering communication services to residents; (vi) a corporation; and (vii) a limited liability company or limited liability partnership. (C) Ineligible entities An individual or legal general partnership that is formed with individuals shall not be eligible to obtain a grant, loan, or grant and loan combination under subsection (c). (D) Limitation (i) In general An eligible entity described in this paragraph that provides telecommunications or broadband service to at least 20 percent of the households in the United States may not receive an amount of funds under this section for a fiscal year in excess of 15 percent of the funds authorized and appropriated under subsection (i) for the fiscal year. (ii) States and State agencies and instrumentalities A State or an agency or instrumentality of a State may not, in total, receive an amount of funds under this section for a fiscal year in excess of 15 percent of the funds authorized and appropriated under subsection (i) for the fiscal year. (E) Previous awards An entity to which a grant, loan, or grant and loan combination is made under subsection (c) shall not use the grant, loan, or grant and loan combination to deploy broadband service in a service area in which broadband service is deployed by any other entity that has received a broadband grant or loan from the Rural Utilities Service, the National Telecommunications and Information Administration, the Department of the Treasury, the Federal Communications Commission, or a State broadband grant program, unless the service provided by the other entity does not provide to at least 75 percent of the households in the service area access to broadband service of at least\u2014 (i) a 100-Mbps downstream transmission capacity; and (ii) a 20-Mbps upstream transmission capacity. (2) Equity requirements (A) In general The Secretary may require an entity to provide a cost share in an amount not to exceed 25 percent of the amount of the grant (including the grant in a grant and loan combination) under subsection (c) requested in the application of the entity. (B) Waiver The Secretary may waive the cost share requirement under subparagraph (A) for entities or projects described in subsection (c)(4). (3) Technical assistance and training (A) In general The Secretary may provide to eligible entities described in paragraph (1) that are applying for assistance under this section for a project described in subsection (c)(3)(A) technical assistance and training\u2014 (i) to prepare reports and surveys necessary to request grants, loans, and grant and loan combinations under this section for broadband deployment; (ii) to improve management, including financial management, relating to the proposed broadband deployment; (iii) to prepare applications for grants, loans, and grant and loan combinations under this section; or (iv) to assist with other areas of need identified by the Secretary. (B) Funding Not less than 3 percent and not more than 5 percent of amounts appropriated under subsection (i) to carry out this section for a fiscal year shall be used for technical assistance and training under this paragraph. (e) Broadband service (1) In general Subject to paragraph (2), for purposes of this section, the minimum acceptable level of broadband service for a rural area shall be at least\u2014 (A) a 100-Mbps downstream transmission capacity; and (B) a 100-Mbps upstream transmission capacity. (2) Adjustments At least once every 2 years, the Secretary shall review, and may adjust through notice published in the Federal Register, the minimum acceptable level of broadband service established under paragraph (1) and broadband buildout requirements under paragraph (3) to ensure that high-quality, cost-effective broadband service is provided to rural areas over time. (3) Broadband buildout requirements (A) Definition of broadband buildout requirement In this paragraph, the term broadband buildout requirement means the level of internet service an applicant receiving assistance under this section must agree, at the time the application is finalized, to provide for the duration of any project-related agreement between the applicant and the Department. (B) Establishment of broadband buildout requirements The Secretary shall establish broadband buildout requirements that\u2014 (i) utilize the same metrics used to define the minimum acceptable level of broadband service under paragraph (1); and (ii) reasonably ensure\u2014 (I) the repayment of all loans; and (II) the financed network is technically capable of providing broadband service for the lifetime of any project-related agreement. (C) Substitute service standards for unique service territories (i) In general If an applicant shows that it would be cost prohibitive to meet the broadband buildout requirements established under this paragraph for the entirety of a proposed service territory due to the unique characteristics of the proposed service territory, the Secretary and the applicant may agree to utilize substitute standards for any unserved portion of the project. (ii) Requirement Any substitute service standards described in clause (i) should continue to consider the best technology available to meet the needs of the residents in the unserved area. ;\n**(2)**\nby redesignating subsections (g), (h), and (i) as subsections (f), (g), and (h), respectively;\n**(3)**\nin subsection (f) (as so redesignated)\u2014\n**(A)**\nin the subsection heading, by striking Loans and Loan Guarantees .\u2014 and inserting Loans .\u2014 ; and\n**(B)**\nin paragraph (1)\u2014\n**(i)**\nin the matter preceding subparagraph (A), by striking or loan guarantee ; and\n**(ii)**\nin subparagraph (A)\u2014\n**(I)**\nby striking clause (ii);\n**(II)**\nby striking Secretary\u2014 in the matter preceding clause (i) and all that follows through in the case in the matter preceding subclause (I) of clause (i) and inserting Secretary in the case ; and\n**(III)**\nby redesignating subclauses (I) and (II) as clauses (i) and (ii), respectively, and indenting appropriately;\n**(4)**\nin subsection (g) (as so redesignated), by striking or loan guarantee each place it appears;\n**(5)**\nin subsection (h) (as so redesignated), in paragraph (1), by striking 1974) and inserting 1974 ( 2 U.S.C. 661a )) ; and\n**(6)**\nby striking subsections (j) and (k) and inserting the following:\n(i) Funding (1) Authorization of appropriations There is authorized to be appropriated to the Secretary to carry out subsections (a) through (h) $650,000,000 for each of fiscal years 2026 through 2030, to remain available until expended. (2) Administration Not more than 5 percent of the amounts made available under paragraphs (1) and (3) shall be available to the Secretary for the administration of subsections (a) through (h). (3) Direct funding (A) Rescission There is rescinded the unobligated balance of amounts made available to carry out section 779 of division A of the Consolidated Appropriations Act, 2018 ( Public Law 115\u2013141 ; 132 Stat. 399). (B) Direct funding On the day after the execution of the rescission in subparagraph (A), there is appropriated to the Secretary, out of amounts in the Treasury not otherwise appropriated, an amount equal to the amount rescinded in subparagraph (A), to carry out subsections (a) through (h), to remain available until expended. (j) Additional rural broadband program loans (1) In general The Secretary may provide direct loans in accordance with the requirements under this section, as in effect on the day before the date of enactment of the ReConnecting Rural America Act of 2025 . (2) Authorization of appropriations There is authorized to be appropriated to the Secretary to carry out this subsection $350,000,000 for each of fiscal years 2026 through 2030, to remain available until expended. (k) Termination of authority No grant, loan, or grant and loan combination may be made under this section after September 30, 2030. .\n##### (b) Sunset\nBeginning on the date that is 120 days after the date of enactment of this Act, section 779 of division A of the Consolidated Appropriations Act, 2018 ( Public Law 115\u2013141 ; 132 Stat. 399), shall have no force or effect.",
      "versionDate": "2025-10-30",
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
        "actionDate": "2025-04-30",
        "text": "Referred to the Committee on Agriculture, and in addition to the Committees on Energy and Commerce, and Appropriations, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "3119",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "ReConnecting Rural America Act of 2025",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-11-25T20:34:47Z"
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
      "date": "2025-10-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3084is.xml"
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
      "title": "ReConnecting Rural America Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-06T07:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "ReConnecting Rural America Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-06T07:53:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Rural Electrification Act of 1936 to establish the ReConnect program under that Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-06T07:48:16Z"
    }
  ]
}
```
