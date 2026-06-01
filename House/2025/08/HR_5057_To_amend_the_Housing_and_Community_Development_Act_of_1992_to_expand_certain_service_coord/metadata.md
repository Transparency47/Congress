# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5057?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5057
- Title: Expanding Service Coordinators Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5057
- Origin chamber: House
- Introduced date: 2025-08-26
- Update date: 2025-11-13T09:05:48Z
- Update date including text: 2025-11-13T09:05:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-26: Introduced in House
- 2025-08-26 - IntroReferral: Introduced in House
- 2025-08-26 - IntroReferral: Introduced in House
- 2025-08-26 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-08-26 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-08-26: Introduced in House

## Actions

- 2025-08-26 - IntroReferral: Introduced in House
- 2025-08-26 - IntroReferral: Introduced in House
- 2025-08-26 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-08-26 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-26",
    "latestAction": {
      "actionDate": "2025-08-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5057",
    "number": "5057",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "S000510",
        "district": "9",
        "firstName": "Adam",
        "fullName": "Rep. Smith, Adam [D-WA-9]",
        "lastName": "Smith",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "Expanding Service Coordinators Act of 2025",
    "type": "HR",
    "updateDate": "2025-11-13T09:05:48Z",
    "updateDateIncludingText": "2025-11-13T09:05:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-26",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-26",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-08-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-26",
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
          "date": "2025-08-26T15:02:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-08-26T15:02:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "OH"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "OR"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5057ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5057\nIN THE HOUSE OF REPRESENTATIVES\nAugust 26, 2025 Mr. Smith of Washington (for himself, Mrs. Beatty , and Ms. Bonamici ) introduced the following bill; which was referred to the Committee on Financial Services , and in addition to the Committee on Education and Workforce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Housing and Community Development Act of 1992 to expand certain service coordinator programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Expanding Service Coordinators Act of 2025 .\n#### 2. Expansion of covered service coordinator programs\n##### (a) In general\nSection 671 of the Housing and Community Development Act of 1992 ( 42 U.S.C. 13631 ) is amended by adding at the end the following:\n(g) Prohibition on additional requirements (1) In general Notwithstanding any other provision of law, if a covered federally assisted housing project is eligible to receive amounts under this title to employ or retain a service coordinator, the Secretary may not subject such covered federally assisted housing project to any additional requirements in exchange for such amounts. (2) Rule of construction Nothing in paragraph (1) may be construed to prohibit the Secretary from requiring reasonable reporting, monitoring, or compliance activities necessary for program administration. .\n##### (b) Additional requirements for service coordinators\nSubtitle E of title VI of the Housing and Community Development Act of 1992 ( 42 U.S.C. 13631 et seq. ) is amended by adding at the end the following:\n678. Additional requirements (a) Funding for service coordinator training An owner of a federally assisted housing project shall, each year, reserve not less than $2,500 of amounts received to carry out a covered service coordinator program for use by a service coordinator to access training in areas described in section 802(d)(4) of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 8011(d)(4) ). (b) Service coordinator training reporting requirement A service coordinator operating pursuant to a covered service coordinator program shall, on an annual basis, submit to the Secretary information, as determined appropriate by the Secretary, with respect to training completed by the service coordinator in the preceding year. (c) Grant applications The Secretary may not require an applicant for a grant under a covered service coordinator program to use all of the amounts available to the applicant prior to submitting an application for such grant. (d) Authorization of appropriations There is authorized to be appropriated to the Secretary for the operation of covered service coordinator programs and the continuation of existing congregate service grants for residents of federally assisted housing projects $225,000,000 for each of fiscal years 2026 through 2030. (e) Covered service coordinator program defined The term covered service coordinator program means the service coordinator programs established pursuant to\u2014 (1) this subtitle; (2) section 802 of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 8011 ); (3) section 202 of the Housing Act of 1959 ( 12 U.S.C. 1701q ); and (4) section 8 of the United States Housing Act of 1937 ( 42 U.S.C. 1437f ). .\n##### (c) Provision of services\nSection 202(g)(3) of the Housing Act of 1959 ( 12 U.S.C. 1701q(g)(3) ) is amended by inserting , including with respect to the calculation of initial rents after eligible cost under subsection (c)(2) .\n##### (d) Service coordinator grant program\nTitle II of the Housing Act of 1959 ( 12 U.S.C. 1701q et seq. ) is amended by inserting after section 202b the following:\n202c. Service Coordinator Grant Program (a) In general The Secretary shall establish and administer a competitive grant program to award grants to eligible applicants to employ or retain 1 or more service coordinators to assist residents residing housing assisted under section 202 in accessing supportive services that promote housing stability, health, and aging in place. (b) Responsibilities Service coordinators funded under this section shall\u2014 (1) consult with project owners, tenants, service providers, and others to assess resident needs; (2) coordinate or manage the provision of supportive services; (3) facilitate tenant education and access to programs that improve resident well-being; (4) meet minimum training and experience requirements as set by the Secretary; and (5) carry out other functions as determined appropriate by the Secretary. (c) Eligible uses of grant funds Amounts provided under this section may be used to cover\u2014 (1) salaries and fringe benefits for service coordinators; (2) training and continuing education for service coordinators; and (3) administrative costs directly related to the coordination of supportive services. (d) Grant terms Grants shall be awarded for a term of 3years, subject to the availability of appropriations. (e) Priority In awarding grants, the Secretary shall give priority to owners or operators of a properties assisted under Section 202\u2014 (1) that serve elderly or disabled residents; or (2) are located in persistent poverty counties or underserved rural areas. (f) Program guidance The Secretary shall issue program guidance, including selection criteria and allowable uses of funds, not later than 180 days after the date of enactment of this section. (g) Eligible applicant defined In this section, the term eligible applicant means an owner or operator of a property assisted under Section 202 that is in good standing with the Department of Housing and Urban Development. (h) No requirement To accept services No resident may be required to accept any service provided through the employment of a service coordinator. .\n#### 3. Public Service Loan Forgiveness eligibility\nSection 455(m)(3)(B)(i) of the Higher Education Act of 1965 ( 20 U.S.C. 1087e(m)(3)(B)(i) ) is amended by inserting public service as a service coordinator, after school-based services, .\n#### 4. Expansion of funding for services for public and Indian housing residents\nSection 34 of the United States Housing Act of 1937 ( 42 U.S.C. 1437z\u20136 ) is amended by adding at the end the following:\n(f) Authorization of appropriations There is authorized to be appropriated to the Secretary to carry out this section $45,000,000 for each of fiscal years 2026 through 2030. .\n#### 5. HRSA grants for service coordinators\n##### (a) In general\nThe Secretary of Health and Human Services, acting through the Administrator of the Health Resources and Services Administration, shall establish a program to award 150 grants to eligible properties to fund service coordinators.\n##### (b) Grant period\nA grant awarded under this section shall be for a period of 3 years, and may be renewed.\n##### (c) Definitions\nIn this section:\n**(1) Eligible property**\nThe term eligible property means a housing project with respect to which a person has claimed a credit under section 42(a) of the Internal Revenue Code of 1986.\n**(2) Service coordinator**\nThe term service coordinator has the meaning given the term in section 671 of the Housing and Community Development Act of 1992.\n##### (d) Authorization of appropriations\nThere is authorized to be appropriated in fiscal year 2026 to carry out this section $37,000,000.\n#### 6. Rural Housing Service Coordinator Grant Program\nTitle V of the Housing Act of 1949 ( 42 U.S.C. 1471 et seq. ) is amended by inserting after section 515 the following:\n515A. Rural Housing Service Coordinator Grant Program (a) In general The Secretary, acting through the Rural Housing Service, shall establish and administer a competitive grant program to award grants to eligible applicants to employ or retain 1 or more service coordinators to assist residents residing in properties assisted under Section 515 in accessing supportive services that promote housing stability, health, and aging in place. (b) Responsibilities Service coordinators funded under this section shall\u2014 (1) consult with project owners, tenants, service providers, and others to assess resident needs; (2) coordinate or manage the provision of supportive services; (3) facilitate tenant education and access to programs that improve resident well-being; (4) meet minimum training and experience requirements as set by the Secretary; and (5) carry out other functions as determined appropriate by the Secretary. (c) Eligible uses of grant funds Amounts provided under this section may be used to cover\u2014 (1) salaries and fringe benefits for service coordinators; (2) training and continuing education for service coordinators; and (3) administrative costs directly related to the coordination of supportive services. (d) Grant terms Grants shall be awarded for a term of 3years, subject to the availability of appropriations. (e) Priority In awarding grants, the Secretary shall give priority to owners or operators of a properties assisted under Section 515\u2014 (1) that serve elderly or disabled residents; or (2) are located in persistent poverty counties or underserved rural areas. (f) Program guidance The Secretary shall issue program guidance, including selection criteria and allowable uses of funds, not later than 180 days after the date of enactment of this section. (g) Eligible applicant defined In this section, the term eligible applicant means an owner or operator of a property assisted under Section 515 that is in good standing with the Department of Agriculture. (h) No requirement To accept services No resident may be required to accept any service provided through the employment of a service coordinator. (i) Authorization of appropriations There is authorized to be appropriated to the Secretary to carry out this section $10,000,000 for fiscal year 2026 and each year thereafter, to remain available until expended. .",
      "versionDate": "2025-08-26",
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
        "name": "Housing and Community Development",
        "updateDate": "2025-09-22T14:52:01Z"
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
      "date": "2025-08-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5057ih.xml"
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
      "title": "Expanding Service Coordinators Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-03T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Expanding Service Coordinators Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-03T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Housing and Community Development Act of 1992 to expand certain service coordinator programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-03T05:18:22Z"
    }
  ]
}
```
