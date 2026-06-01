# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8185?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8185
- Title: HELP Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8185
- Origin chamber: House
- Introduced date: 2026-04-02
- Update date: 2026-04-17T19:44:48Z
- Update date including text: 2026-04-17T19:44:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-02: Introduced in House
- 2026-04-02 - IntroReferral: Introduced in House
- 2026-04-02 - IntroReferral: Introduced in House
- 2026-04-02 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2026-04-02: Introduced in House

## Actions

- 2026-04-02 - IntroReferral: Introduced in House
- 2026-04-02 - IntroReferral: Introduced in House
- 2026-04-02 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-02",
    "latestAction": {
      "actionDate": "2026-04-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8185",
    "number": "8185",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "P000617",
        "district": "7",
        "firstName": "Ayanna",
        "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
        "lastName": "Pressley",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "HELP Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-17T19:44:48Z",
    "updateDateIncludingText": "2026-04-17T19:44:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-02",
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
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-02",
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
          "date": "2026-04-02T12:30:15Z",
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
      "bioguideId": "D000216",
      "district": "3",
      "firstName": "Rosa",
      "fullName": "Rep. DeLauro, Rosa L. [D-CT-3]",
      "isOriginalCosponsor": "True",
      "lastName": "DeLauro",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-04-02",
      "state": "CT"
    },
    {
      "bioguideId": "G000585",
      "district": "34",
      "firstName": "Jimmy",
      "fullName": "Rep. Gomez, Jimmy [D-CA-34]",
      "isOriginalCosponsor": "True",
      "lastName": "Gomez",
      "party": "D",
      "sponsorshipDate": "2026-04-02",
      "state": "CA"
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
      "sponsorshipDate": "2026-04-02",
      "state": "DC"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-04-02",
      "state": "MI"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2026-04-02",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8185ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8185\nIN THE HOUSE OF REPRESENTATIVES\nApril 2, 2026 Ms. Pressley (for herself, Ms. DeLauro , Mr. Gomez , Ms. Norton , Ms. Tlaib , and Ms. Jayapal ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo create a database of eviction information, establish grant programs for eviction prevention and legal aid, and limit use of housing court-related records in consumer reports, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Housing Emergencies Lifeline Program Act of 2026 or the HELP Act of 2026 .\n#### 2. Database of eviction information\n##### (a) Reports by housing providers\n**(1) In general**\nThe Secretary of Housing and Urban Development shall require each State and local entity that receives covered housing assistance to submit to the Secretary annual reports under this section regarding evictions from assisted dwelling units of the covered housing occurring during the preceding year.\n**(2) Contents**\nEach report submitted pursuant to subsection (a) shall include\u2014\n**(A)**\nfor each household subject to an eviction proceeding during the year which the report covers\u2014\n**(i)**\nthe reason or reasons that the eviction proceeding was undertaken and, in the case of any eviction proceeding undertaken in whole or in part based on an arrearage in rent owed, the amount of such arrearage and the amount of the tenant\u2019s required contribution toward rent;\n**(ii)**\nthe date on which the household was ordered to be evicted;\n**(iii)**\nthe address of the dwelling unit from which the household was evicted;\n**(iv)**\nwhether the household was represented by legal counsel in any eviction proceeding, if such information is available;\n**(v)**\nthe number of days the household was given to vacate the dwelling unit, if such information is available; and\n**(vi)**\nwhether a writ of execution was issued in regards to the eviction; and\n**(B)**\nfor each individual in any household subject to an eviction proceeding during the year which the report covers\u2014\n**(i)**\nthe name of the individual;\n**(ii)**\nthe annual income of the individual in the fiscal year prior to the year during which the individual was evicted, if available;\n**(iii)**\nthe disability status of the individual evicted, if available;\n**(iv)**\nany available demographic information about the individual including race, ethnicity, age, and gender;\n**(v)**\nany foster care history for the individual, if available;\n**(vi)**\nany serious physical health problems or serious mental illness of the individual, if such information is available;\n**(vii)**\nany history of prior homelessness of the individual, if such information is available; and\n**(viii)**\nwhether the individual has a criminal record, if such information is available.\n**(3) Data requirements**\nThe Secretary of Housing and Urban Development shall develop requirements for States and local entities that receive covered housing assistance that\u2014\n**(A)**\nprovides limitations on how long the information described in paragraph (2) shall be retained; and\n**(B)**\nestablishes data privacy and security requirements for the information described in paragraph (2) that\u2014\n**(i)**\nincludes appropriate measures to ensure that the privacy of the individuals and households is protected and that the information, including any personally identifiable information, is collected and used only for the purpose of submitting reports under paragraph (1); and\n**(ii)**\nensures that any names collected are redacted and replaced with an anonymous identifier.\n##### (b) Database\n**(1) In general**\nThe Secretary shall establish a database for collecting and maintaining information submitted in reports pursuant to subsection (a).\n**(2) Disaggregation**\nTo the extent possible, such database shall be disaggregated by the smallest census tract, block group, or block possible for the data set, and by income, race, gender, disability, and all other protected classes under the Fair Housing Act.\n**(3) Privacy protections**\nThe Secretary shall establish appropriate measures regarding information in the database to ensure that, subject to paragraph (3), the privacy of the individuals and households is protected and that any personally identifiable information is not disclosed, including by redacting all names.\n**(4) Research**\nThe Secretary may make full and unredacted information available to academic institutions for the purpose of researching causes and solutions to evictions and adherence to civil rights protections.\n#### 3. Eviction protection grant program\n##### (a) Establishment\nThe Secretary shall establish a grant program to award competitive grants to eligible entities as described in this section.\n##### (b) Eligibility\nTo be eligible for a grant under this section, an entity shall be a nonprofit or government entity.\n##### (c) Eligible uses\nAn entity that is awarded a grant under this section shall use such grant to provide legal assistance (including assistance related to pretrial activities, trial activities, post-trial activities and alternative dispute resolution) at no cost to eligible low-income tenants at risk of or subject to eviction.\n##### (d) Priority\nIn awarding grants under this section, the Secretary shall give preference to eligible entities that\u2014\n**(1)**\ninclude a marketing strategy for residents of areas with high rates of eviction;\n**(2)**\nhave experience providing no-cost legal assistance to low-income individuals, including those with limited English proficiency or disabilities; and\n**(3)**\nhave sufficient capacity to administer such assistance.\n##### (e) Use in urban and rural areas\nThe Secretary shall ensure, to the extent practicable, that the proportion of tenants living in rural areas who will receive legal assistance with grant amounts under this section is not less than the overall proportion of tenants who live in rural areas.\n##### (f) Authorization of appropriations\nThere is authorized to be appropriated to the Secretary such sums as needed for\u2014\n**(1)**\ngrants under this section; and\n**(2)**\nassistance under the emergency solutions grants program under subtitle B of title IV of the McKinney-Vento Homeless Assistance Act ( 42 U.S.C. 11371 et seq. ), to be used only for\u2014\n**(A)**\nproviding legal counsel for tenants subject to or at risk of eviction with regard to any eviction related legal proceeding; and\n**(B)**\ncosts of any court fees associated with an eviction-related legal proceeding for a tenant (excluding any attorneys fees for the attorney of the landlord of the tenant).\n#### 4. Consumer reports\n##### (a) In general\nSection 605(a) of the Fair Credit Reporting Act ( 15 U.S.C. 1681c(a) ) is amended by adding at the end the following:\n(9) An eviction, or any information related to an eviction or a proceeding seeking eviction, of a consumer from a rental dwelling. (10) Any adverse item of information related to rent or utility arrears. .\n##### (b) Applicability\nThe amendment made by this section shall apply to any consumer report (as defined in section 603 of the Fair Credit Reporting Act ( 15 U.S.C. 1681a )) issued on or after the date of the enactment of this Act.\n#### 5. Eviction information\n##### (a) In general\nThe Secretary shall, not later than 1 year after the date of the enactment of this Act, issue rules that require each owner of a covered federally assisted rental dwelling unit to ensure that each tenant of such dwelling unit owned by such owner receives information, in writing\u2014\n**(1)**\nnot less than once each year regarding\u2014\n**(A)**\nthe rights and responsibilities of such owner with regard to eviction; and\n**(B)**\nlocal organizations and resources that can provide assistance in eviction-related matters;\n**(2)**\nupon provision of any notice of eviction, stating the reason or reasons for the eviction; and\n**(3)**\nall notices given shall clarify that rights and responsibilities of tenants are subject to State and local law.\n##### (b) Hotline\nThe Secretary shall, not later than 1 year after the date of the enactment of this Act, establish a hotline to provide assistance with regard to eviction-related matters to tenants of covered federally assisted rental dwelling units. The Secretary shall establish guidance to ensure that the hotline is visible, promoted to consumers, is accessible in English and other languages, has accommodations for those who have disabilities, and maintains adequate staff to match the volume of calls to the hotline. Assistance must direct callers to available resources, including legal aid, and make callers aware of their rights and responsibilities as tenants.\n#### 6. Definitions\nIn this Act:\n**(1) Assistance**\nThe term assistance means any grant, loan, subsidy, contract, cooperative agreement, or other form of financial assistance, but such term does not include the insurance or guarantee of a loan, mortgage, or pool of loans or mortgages.\n**(2) Covered federally assisted rental dwelling unit**\nThe term covered federally assisted rental dwelling unit means a residential dwelling unit that\u2014\n**(A)**\nis made available for rental; and\n**(B)**\n**(i)**\nfor which assistance is provided, or that is part of a housing project for which assistance is provided, under any program administered by the Secretary of Housing and Urban Development, including\u2014\n**(I)**\nthe public housing program under the United States Housing Act of 1937 21 ( 42 U.S.C. 1437 et seq. );\n**(II)**\nthe program for rental assistance under section 8 of the United States Housing Act of 1937 ( 42 U.S.C. 1437f );\n**(III)**\nthe HOME Investment Partnerships program under title II of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 12721 et seq. );\n**(IV)**\ntitle IV of the McKinney-Vento Homeless Assistance Act ( 42 U.S.C. 11360 et seq. );\n**(V)**\nthe Housing Trust Fund program under section 1338 of the Housing and Community Development Act of 1992 ( 12 U.S.C. 4568 );\n**(VI)**\nthe program for supportive housing for the elderly under section 202 of the Housing Act of 1959 ( 12 U.S.C. 1701q );\n**(VII)**\nthe program for supportive housing for persons with disabilities under section 811 of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 8013 );\n**(VIII)**\nthe AIDS Housing Opportunities program under subtitle D of title VIII of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 12901 et seq. );\n**(IX)**\nthe program for Native American housing under the Native American Housing Assistance and Self-Determination Act of 1996 ( 25 U.S.C. 4101 et seq. ); and\n**(X)**\nthe program for housing assistance for Native Hawaiians under title VIII of the Native American Housing Assistance and Self-Determination Act of 1996 7 ( 25 U.S.C. 4221 et seq. ); or\n**(ii)**\nis a property, or is on or in a property, that has a federally backed mortgage loan or federally backed multifamily mortgage loan, as 11 such terms are defined in section 4024(a) of the CARES Act ( 15 U.S.C. 9058(a) ).\n**(3) Covered housing**\nThe term covered housing means a dwelling unit assisted with amounts made available, or a loan or mortgage made, insured, or guaranteed, under any of the following programs:\n**(A)**\nThe programs for tenant- and project-based rental assistance under section 8 of the United States Housing Act of 1937 (42 U.S.C. 21 1437f).\n**(B)**\nThe program for public housing under the United States Housing Act of 1937 (42 24 U.S.C. 1437 et seq. ).\n**(C)**\nThe program for supportive housing for the elderly under section 202 of the Housing Act of 1959 ( 12 U.S.C. 1701q ).\n**(D)**\nThe program for supportive housing for persons with disabilities under section 811 of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 8013 ).\n**(E)**\nThe community development block grant program under title I of the Housing and Community Development Act of 1974 (42 11 U.S.C. 5301 et seq. ).\n**(F)**\nThe HOME Investment Partnerships program under titles I and II of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 12704 et seq. ).\n**(G)**\nThe program for housing opportunities for persons with AIDS under subtitle D of title VIII of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 12901 et seq. ).\n**(H)**\nThe programs for homeless assistance under title IV of the Mckinney-Vento Homeless Assistance Act ( 42 U.S.C. 11361 et seq. ).\n**(4) Covered housing assistance**\nThe term covered housing assistance means assistance under any program specified in paragraph (3).\n**(5) Legal counsel**\nThe term legal counsel means full representation by an attorney throughout proceedings in issue.\n**(6) Owner**\nFor the purposes of this Act, the term owner means any private person or entity, including a cooperative, an agency of the Federal Government, or a public housing agency, having the legal right to lease or sublease dwelling units.\n**(7) Secretary**\nThe term Secretary means Secretary of Housing and Urban Development.",
      "versionDate": "2026-04-02",
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
        "updateDate": "2026-04-17T19:44:48Z"
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
      "date": "2026-04-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8185ih.xml"
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
      "title": "HELP Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-14T05:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HELP Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-14T05:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Housing Emergencies Lifeline Program Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-14T05:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To create a database of eviction information, establish grant programs for eviction prevention and legal aid, and limit use of housing court-related records in consumer reports, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-14T05:18:36Z"
    }
  ]
}
```
