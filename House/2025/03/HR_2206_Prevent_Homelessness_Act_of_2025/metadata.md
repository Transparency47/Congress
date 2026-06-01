# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2206?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2206
- Title: Prevent Homelessness Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2206
- Origin chamber: House
- Introduced date: 2025-03-18
- Update date: 2025-05-10T08:05:44Z
- Update date including text: 2025-05-10T08:05:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-18: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-03-18: Introduced in House

## Actions

- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-18",
    "latestAction": {
      "actionDate": "2025-03-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2206",
    "number": "2206",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "L000582",
        "district": "36",
        "firstName": "Ted",
        "fullName": "Rep. Lieu, Ted [D-CA-36]",
        "lastName": "Lieu",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Prevent Homelessness Act of 2025",
    "type": "HR",
    "updateDate": "2025-05-10T08:05:44Z",
    "updateDateIncludingText": "2025-05-10T08:05:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-18",
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
      "actionDate": "2025-03-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-18",
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
          "date": "2025-03-18T16:07:45Z",
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
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "CA"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "IL"
    },
    {
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "False",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2025-05-09",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2206ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2206\nIN THE HOUSE OF REPRESENTATIVES\nMarch 18, 2025 Mr. Lieu (for himself, Mr. Mullin , and Mr. Jackson of Illinois ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo establish a Housing Stabilization Fund to provide emergency housing assistance to extremely low-income renters and homeowners, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Prevent Homelessness Act of 2025 .\n#### 2. Housing Stabilization Fund\n##### (a) Establishment\nThe Secretary of Housing and Urban Development, acting through the Office of Special Needs Assistance Programs of the Office of Community Planning and Development, shall establish and administer a fund to be known as the Housing Stabilization Fund.\n##### (b) Grants\nAmounts in the Fund shall be available, to the extent provided in advance in appropriations Acts, only for making annual grants under this section, in the amount determined pursuant to subsection (f), to continua of care to provide short-term assistance under emergency housing assistance programs that the Secretary determines, pursuant to applications under subsection (e), meet the requirements of subsection (c).\n##### (c) Emergency housing assistance program requirements\nAn emergency housing assistance program shall be considered to meet the requirements of this subsection only if the program\u2014\n**(1)**\nis carried out by a continuum of care or other agency, organization, or entity selected by a continuum of care;\n**(2)**\noperates within the geographical area served by the continuum of care;\n**(3)**\nprovides financial assistance only on behalf of extremely low-income families and very low-income families who\u2014\n**(A)**\nare unable to meet housing-related obligations (as described in subsection (d) of this section) due to a financial hardship, which shall include the situations described in clause (i) of section 3(a)(3)(B) of the United States Housing Act of 1937 ( 42 U.S.C. 1437a(a)(3)(B)(i) ), a family or health crisis, unexpected expenses, unsafe or unhealthy living conditions, and such other situations as the Secretary may provide; and\n**(B)**\nprovide evidence of such inability to meet housing related obligations, which may include past-due utilities or rent notices, eviction notices, and such other evidence as the Secretary may provide, except that a continuum of care may, in consultation with the Secretary, provide for additional manners of identifying inability to meet housing related obligations in situations in which such notices are not available;\n**(4)**\nprovides for coordination with any local homeless prioritization criteria, including the Coordinated Entry System or any other evidence-based analytic targeting tool, applicable within the area in which the program will be carried out, in accordance with such requirements as the Secretary shall provide; and\n**(5)**\nmeets such other requirements as the Secretary may establish.\n##### (d) Eligible financial assistance\nAmounts from grants under this section for an emergency housing assistance program shall be used to provide financial assistance only to meet housing-related obligations, including\u2014\n**(1)**\nprospective rent due, except that such assistance may not\u2014\n**(A)**\nbe provided for a family for more than 8 months (whether consecutive or not) within the preceding 12 months; or\n**(B)**\nexceed on a monthly basis the amount that the Secretary determines is reasonable in comparison with rents charged for comparable dwelling units located in the same area in the private, unassisted local market;\n**(2)**\nrental arrears, with payments based on actual rent amount due;\n**(3)**\nmortgage payments due, including amounts past due, except that such assistance may not be provided for a household for more than 8 months (whether consecutive or not) within the preceding 12 months and may not exceed on a monthly basis such amount as the Secretary shall determine;\n**(4)**\nutility payments due, including amounts past due;\n**(5)**\nhousing repairs necessary to make the premises habitable, including installing insulation, window repair, door repair, roof repair, and other repairs;\n**(6)**\ncosts of obtaining services for behavioral, emotional, and mental health issues, domestic violence issues, child welfare issues, employment counseling, substance abuse treatment, or other services;\n**(7)**\ncosts of obtaining housing counseling or advice, including outreach, mediation, and case management;\n**(8)**\ncosts of obtaining legal assistance relating to eviction, foreclosure, and other issues relating to a family retaining its housing;\n**(9)**\nsecurity deposit payments due; and\n**(10)**\nother short-term costs the payment of which increase housing stability for an extremely low-income family or a very low-income family, including costs for gas, groceries, automotive repair, public transportation, furniture, application fees, reunification services, and such other costs as the Secretary may provide.\n##### (e) Applications\nThe Secretary shall require, for a continuum of care to receive a grant under this section for a fiscal year, that the continuum of care submit to the Secretary, and the Secretary approve, an application containing such information as the Secretary considers necessary to ensure that grant amounts are used in accordance with this section.\n##### (f) Amount of grants\n**(1) Allocation**\n**(A) Fiscal year 2027**\nFor fiscal year 2027, any amounts made available from the Fund for grants under this section shall be allocated for grants to continua of care according to the formula established pursuant to paragraph (2).\n**(B) Succeeding fiscal years**\nFor each fiscal year thereafter, of any amounts made available from the Fund for grants under this section\u2014\n**(i)**\n80 percent shall be allocated for grants to continua of care according to the formula established pursuant to paragraph (2); and\n**(ii)**\n20 percent shall be allocated for grants to continua of care according to a competition pursuant to paragraph (3).\n**(2) Formula**\n**(A) In general**\nThe Secretary shall, by regulation, establish a formula for use to allocate amounts in the Fund for grants for a fiscal year, in accordance with paragraph (1), for continua of care whose applications for such year for such assistance have been approved pursuant to subsection (e).\n**(B) Factors**\nThe formula required by subparagraph (A) shall be designed to take into consideration, for the area served by a continuum of care\u2014\n**(i)**\nthe extent of the population that are extremely low-income families, including the homeless population that is unsheltered, who are severely cost-burdened by housing-related costs, including obligations described in subsection (d);\n**(ii)**\nthe extent of the population that are very low-income families; and\n**(iii)**\nsuch other factors as the Secretary may provide.\nThe Secretary shall determine data to be used for the factors considered under the formula based on the most recently conducted Point-In-Time Homeless Count administered by the Secretary.\n**(3) Competition**\nThe Secretary shall, by regulation, establish a competition for use to allocate amounts in the Fund for grants for a fiscal year for continua of care pursuant to paragraph (1)(B)(ii), which shall be based on measurable criteria that\u2014\n**(A)**\nto the greatest extent possible, are required to be collected and reported to the Department of Housing and Urban Development or any other Federal agency under other provisions of law already in effect or otherwise do not impose new burdens on continua of care;\n**(B)**\nprovide for targeting of assistance made available under an emergency housing assistance program to households having the lowest incomes;\n**(C)**\nencourage the leveraging of other non-Federal funds for providing assistance under an emergency housing assistance program;\n**(D)**\nencourage emergency housing assistance programs assisted with grants under this section to provide preventive assistance to avoid homelessness; and\n**(E)**\nencourage problem-solving and diversion methods, including the applicant\u2019s capacity and interest in providing innovative delivery of housing stability interventions and connecting households to other public benefits that promote housing stability.\n##### (g) Definitions\nFor purposes of this Act, the following definitions shall apply:\n**(1) Continuum of care**\nThe term continuum of care means a collaborative applicant established and operating for a geographic area for purposes of the Continuum of Care Program under subtitle C of title IV of the McKinney-Vento Homeless Assistance Act ( 42 U.S.C. 11381 et seq. ).\n**(2) Extremely low-income family; very low-income family**\nThe terms extremely low-income family and very low-income family have the meanings given such terms in section 3(b) of the United States Housing Act of 1937 ( 42 U.S.C. 1437a(b) ).\n**(3) Fund**\nThe term Fund means the Housing Stabilization Fund established under subsection (a).\n**(4) Secretary**\nThe term Secretary means the Secretary of Housing and Urban Development.\n##### (h) Authorization of appropriations\nThere is authorized to be appropriated for the Fund $100,000,000 for each of fiscal years 2027 through 2031.",
      "versionDate": "2025-03-18",
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
        "updateDate": "2025-04-01T17:27:47Z"
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
      "date": "2025-03-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2206ih.xml"
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
      "title": "Prevent Homelessness Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-01T04:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Prevent Homelessness Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-01T04:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a Housing Stabilization Fund to provide emergency housing assistance to extremely low-income renters and homeowners, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-01T04:18:32Z"
    }
  ]
}
```
