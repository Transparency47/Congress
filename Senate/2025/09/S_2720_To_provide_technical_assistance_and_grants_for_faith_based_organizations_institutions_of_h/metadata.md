# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2720?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2720
- Title: Yes in God's Backyard Act
- Congress: 119
- Bill type: S
- Bill number: 2720
- Origin chamber: Senate
- Introduced date: 2025-09-04
- Update date: 2026-02-18T17:17:03Z
- Update date including text: 2026-02-18T17:17:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-04: Introduced in Senate
- 2025-09-04 - IntroReferral: Introduced in Senate
- 2025-09-04 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-09-04: Introduced in Senate

## Actions

- 2025-09-04 - IntroReferral: Introduced in Senate
- 2025-09-04 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-04",
    "latestAction": {
      "actionDate": "2025-09-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2720",
    "number": "2720",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "W000805",
        "district": "",
        "firstName": "Mark",
        "fullName": "Sen. Warner, Mark R. [D-VA]",
        "lastName": "Warner",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Yes in God's Backyard Act",
    "type": "S",
    "updateDate": "2026-02-18T17:17:03Z",
    "updateDateIncludingText": "2026-02-18T17:17:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-04",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-04",
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
          "date": "2025-09-04T17:46:57Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "DE"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "NJ"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "MD"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "False",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "HI"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2720is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2720\nIN THE SENATE OF THE UNITED STATES\nSeptember 4, 2025 Mr. Warner (for himself, Ms. Blunt Rochester , Mr. Kim , and Ms. Alsobrooks ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo provide technical assistance and grants for faith-based organizations, institutions of higher education, and local governments to increase the supply of affordable rental housing, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Yes in God's Backyard Act .\n#### 2. Technical assistance and grants for faith-based organizations, institutions of higher education, and local governments to remove barriers to and increase the supply of affordable rental housing\nTitle II of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 12721 et seq. ), is amended by adding at the end the following:\nG Technical assistance and grants for faith-based organizations, institutions of higher education, and local governments to remove barriers and to increase the supply of affordable rental housing 290. Definitions In this subtitle: (1) Affordable rental housing The term affordable rental housing means housing available to the public charging a monthly rent that is not more than 30 percent of household income of a covered household. (2) At risk of homelessness The term at risk of homelessness has the meaning given the term in section 401 of the McKinney-Vento Homeless Assistance Act ( 42 U.S.C. 11360 ). (3) Covered household The term covered household means a household with income that is at or below 100 percent of area median income as defined by the Secretary. (4) Extremely low-income families The term extremely low-income families has the meaning given the term in section 3(b) of the United States Housing Act of 1937 ( 42 U.S.C. 1437a ). (5) Faith-based organization The term faith-based organization \u2014 (A) has the meaning given the term by the Secretary; and (B) includes any organization assisted by the Partnership Center. (6) Homeless The term homeless has the meaning given the term in section 103 of the McKinney-Vento Homeless Assistance Act ( 42 U.S.C. 11302 ). (7) Institution of higher education The term institution of higher education has the meaning given the term in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 ). (8) Partnership center The term Partnership Center means the Center for Faith-Based and Neighborhood Partnerships in the Office of the Secretary or any successor office. 291. Technical assistance program (a) Program The Secretary shall establish a program to provide technical assistance to assist faith-based organizations, institutions of higher education, and local governments in order to remove barriers to the production and preservation of affordable rental housing on property owned by faith-based organizations and institutions of higher education. (b) Contents The program established under subsection (a) shall consist of resources related to\u2014 (1) understanding how excess property owned by faith-based organizations and institutions of higher education can be developed into affordable rental housing and how existing affordable rental housing can be preserved; (2) the development and preservation of affordable rental housing on property owned by faith-based organizations and institutions of higher education, including\u2014 (A) housing for households at or below 60 percent of area median income; (B) housing for individuals and families who are homeless or at risk of homelessness, including veterans; (C) accessible rental housing for individuals with disabilities; (D) housing for intergenerational families under section 203 of the LEGACY Act of 2003 ( 12 U.S.C. 1701q note); (E) housing for other special needs populations as determined by the Secretary; and (F) housing that would increase equitable access to well-resourced areas of opportunity; (3) Federal assistance for affordable rental housing production and preservation, including information on federally assisted rental housing programs, and services for residents; (4) best practices in the housing development and preservation processes, including selection of development, preservation, and management partners, considerations regarding land lease, ownership, or sale ensuring equitable access to housing, and other considerations; (5) best practices for State and local governments to remove barriers to and encourage the production of affordable rental housing, especially in well-resourced areas of opportunity, on property owned by faith-based organizations and institutions of higher education; and (6) any other areas as determined by the Secretary. (c) Consultation In developing technical assistance and other resources under this section, the Secretary shall consult with the Partnership Center and other Federal agencies administering affordable housing and related programs, including the Departments of Agriculture, the Treasury, and Health and Human Services. (d) Dissemination The resources described in subsection (b) shall be made publicly available. (e) Authorization of appropriations There is authorized to be appropriated to carry out this section\u2014 (1) $25,000,000 for fiscal year 2026; and (2) $10,000,000 each of fiscal years 2027 through 2031. 292. Challenge grants to remove barriers to and increase affordable rental housing supply on property owned by faith-based organizations and institutions of higher education (a) Definitions In this section: (1) Eligible grantee The term eligible grantee means\u2014 (A) a unit of general local government; (B) a State; (C) a metropolitan planning organization; and (D) a multi-jurisdiction entity, as defined by the Secretary. (2) State; unit of general local government The terms State and unit of general local government have the meanings given those terms in section 102 of the Housing and Community Development Act of 1974 ( 42 U.S.C. 5302 ). (b) Establishment The Secretary shall establish a Challenge Grant program to make grants on a competitive basis to eligible grantees that have policies in effect that are designed to remove barriers to the production and preservation of affordable rental housing on property owned by faith-based organizations and institutions of higher education. (c) Application (1) In general An eligible entity desiring a grant under this section shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require. (2) Other requirements In order to receive a grant under this section, an applicant shall\u2014 (A) demonstrate that the applicant has policies in effect designed to remove barriers to the production or preservation of affordable housing on property owned by faith-based organizations and institutions of higher education, as determined by the Secretary; (B) make publicly available a proposed plan for use of a grant under this section and solicit comments on the plan; and (C) address the disposition of public comments described in subparagraph (B) in a final plan submitted to the Secretary as part of the grant application. (d) Preference In making awards under this section, the Secretary shall give preference to applicants that propose to use the grant to produce or preserve\u2014 (1) affordable rental housing for families with incomes below 60 percent of area median income, as determined by the Secretary in well-resourced areas of opportunity; (2) affordable rental housing for extremely low-income families; (3) affordable rental housing or non-congregate emergency housing for individuals and families who are homeless or at risk of homelessness, including veterans; (4) affordable and accessible rental housing for individuals with disabilities; (5) affordable rental housing for intergenerational families under section 203 of the LEGACY Act of 2003 ( 12 U.S.C. 1701q note); or (6) affordable rental housing for other special needs populations as designated by the Secretary. (e) Allowable uses An eligible entity that receives a grant under this section shall use grant funds to carry out 1 or more of the following activities pertaining to the removal of barriers to and encouraging the production and preservation of affordable rental housing on property owned by faith-based organizations and institutions of higher education: (1) Assessing and removing local policy and procedural barriers to and adopting best practices to encourage the development of affordable rental housing under this section. (2) Outreach to and technical assistance for faith-based organizations, institutions of higher education, and other community partners to facilitate production and preservation of affordable rental housing. (3) Making grants and loans to projects that produce or preserve affordable rental housing under this section. (4) Such other activities that will further the purposes of this subtitle, as determined by the Secretary. (f) Reporting and data collection A grantee under this section shall submit such information as the Secretary may require in order to monitor, assist, and evaluate the performance of the grantee and program under this section. (g) Authorization of appropriations (1) In general There is authorized to be appropriated to carry out this section $50,000,000 for each of fiscal years 2026 through 2031. (2) Administrative costs Of the funds authorized to be appropriated under paragraph (1), not more than 10 percent may be used by the Secretary for administering the grant program established under this section. .",
      "versionDate": "2025-09-04",
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
        "actionDate": "2026-01-20",
        "text": "Referred to the House Committee on Financial Services."
      },
      "number": "7152",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Yes in God's Backyard Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-01-07",
        "text": "Referred to the House Committee on Financial Services."
      },
      "number": "6957",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Yes in God's Backyard Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Disability assistance",
            "updateDate": "2026-02-06T19:26:22Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-02-06T19:26:22Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2026-02-06T19:26:22Z"
          },
          {
            "name": "Homelessness and emergency shelter",
            "updateDate": "2026-02-06T19:26:22Z"
          },
          {
            "name": "Housing and community development funding",
            "updateDate": "2026-02-06T19:26:22Z"
          },
          {
            "name": "Housing supply and affordability",
            "updateDate": "2026-02-06T19:26:22Z"
          },
          {
            "name": "Low- and moderate-income housing",
            "updateDate": "2026-02-06T19:26:22Z"
          },
          {
            "name": "Religion",
            "updateDate": "2026-02-06T19:26:22Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2026-02-06T19:26:22Z"
          }
        ]
      },
      "policyArea": {
        "name": "Housing and Community Development",
        "updateDate": "2025-09-23T15:06:20Z"
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
      "date": "2025-09-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2720is.xml"
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
      "title": "Yes in God's Backyard Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-11T04:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Yes in God's Backyard Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-11T04:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide technical assistance and grants for faith-based organizations, institutions of higher education, and local governments to increase the supply of affordable rental housing, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-11T04:48:32Z"
    }
  ]
}
```
