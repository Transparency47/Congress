# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1981?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1981
- Title: Choice in Affordable Housing Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1981
- Origin chamber: House
- Introduced date: 2025-03-10
- Update date: 2026-01-31T03:36:14Z
- Update date including text: 2026-01-31T03:36:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-10: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-03-10: Introduced in House

## Actions

- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-10",
    "latestAction": {
      "actionDate": "2025-03-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1981",
    "number": "1981",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "C001061",
        "district": "5",
        "firstName": "Emanuel",
        "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
        "lastName": "Cleaver",
        "party": "D",
        "state": "MO"
      }
    ],
    "title": "Choice in Affordable Housing Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-31T03:36:14Z",
    "updateDateIncludingText": "2026-01-31T03:36:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-10",
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
      "actionDate": "2025-03-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-10",
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
          "date": "2025-03-10T16:00:30Z",
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "NY"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "IL"
    },
    {
      "bioguideId": "G000589",
      "district": "5",
      "firstName": "Lance",
      "fullName": "Rep. Gooden, Lance [R-TX-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gooden",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "TX"
    },
    {
      "bioguideId": "L000562",
      "district": "8",
      "firstName": "Stephen",
      "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Lynch",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "MA"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "AZ"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-09-09",
      "state": "PA"
    },
    {
      "bioguideId": "L000557",
      "district": "1",
      "firstName": "John",
      "fullName": "Rep. Larson, John B. [D-CT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Larson",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1981ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1981\nIN THE HOUSE OF REPRESENTATIVES\nMarch 10, 2025 Mr. Cleaver (for himself, Mr. Lawler , Mr. Casten , Mr. Gooden , Mr. Lynch , and Mr. Ciscomani ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo increase the number of landlords participating in the Housing Choice Voucher program.\n#### 1. Short title\nThis Act may be cited as the Choice in Affordable Housing Act of 2025 .\n#### 2. Definitions\nIn this Act\u2014\n**(1)**\nthe term Housing Choice Voucher program means the tenant-based assistance program under section 8(o) of the United States Housing Act of 1937 ( 42 U.S.C. 1437f(o) );\n**(2)**\nthe term Secretary means the Secretary of Housing and Urban Development; and\n**(3)**\nthe term Tribal Housing and Urban Development-Veterans Affairs Supportive Housing program means the demonstration program established under paragraph (5) under the heading Tenant-based rental assistance under the heading Public and Indian Housing in title II of division K of the Consolidated and Further Continuing Appropriations Act, 2015 ( Public Law 113\u2013235 ; 128 Stat. 2732) (commonly known as Tribal HUD\u2013VASH ).\n#### 3. Findings\nCongress finds the following:\n**(1)**\nThe Housing Choice Voucher program is the Federal Government's largest program helping low-income families, the elderly, and persons with disabilities to afford decent, safe, and sanitary housing in the private market.\n**(2)**\nThe Housing Choice Voucher program is proven to have positive impacts on voucher holders, including increased housing stability, reduced homelessness, and children lifted out of poverty.\n**(3)**\nAs a public-private partnership, the Housing Choice Voucher program relies on the willingness of private landlords to accept vouchers.\n**(4)**\nLandlord participation is declining in the Housing Choice Voucher program, with an average of 10,000 housing providers leaving the program each year between 2010 and 2016.\n**(5)**\nLandlord participation is especially lacking in high-opportunity neighborhoods that have low poverty rates and good access to quality schools, jobs, and public transportation.\n**(6)**\nThe Secretary has conducted and continues to conduct research on landlord participation in the Housing Choice Voucher program.\n**(7)**\nThe Moving to Work demonstration program of the Department of Housing and Urban Development has given participating public housing agencies the ability to test innovative strategies to incentivize landlords to accept vouchers.\n**(8)**\nIndian Tribes and tribally designated housing entities, which do not participate in the Housing Choice Voucher program, benefit from the Tribal Housing and Urban Development-Veterans Affairs Supportive Housing program, which provides rental assistance to Native American veterans who are experiencing or at risk of experiencing homelessness.\n#### 4. Sense of Congress\nIt is the sense of Congress that the Housing Choice Voucher program should be improved to increase the number of landlords, particularly landlords with units in high-opportunity neighborhoods, who accept vouchers in order to expand housing choice and opportunity, and further fair housing.\n#### 5. Incentivizing landlord participation in Housing Choice Voucher program\n##### (a) One-Time incentive payments\nSection 8(o) of the United States Housing Act of 1937 ( 42 U.S.C. 1437f(o) ) is amended by adding at the end the following:\n(23) One-time incentive payments (A) Definition In this paragraph, the term eligible unit means a dwelling unit that\u2014 (i) is located in a census tract with a poverty rate of less than 20 percent; and (ii) has not previously been subject to a housing assistance payment contract under this subsection. (B) Incentive payment authority (i) In general To incentivize landlords who own dwelling units in low-poverty areas to enter into housing assistance payment contracts under this subsection, the Secretary shall provide assistance under this paragraph to public housing agencies to be used to offer a one-time payment directly to the owner of an eligible unit entering into a housing assistance payment contract with the public housing agency for the eligible unit. (ii) Amount The amount of an incentive payment made to an eligible owner under clause (i) may not exceed 200 percent of the monthly housing assistance payment made to the eligible owner for the eligible unit. (iii) Conditions permitted Subject to paragraph (7), a public housing agency may require the owner of an eligible unit, as a condition of receiving an incentive payment under clause (i), to commit to lease the eligible unit to tenants assisted under this subsection for more than 1 year. (iv) Limit The owner of an eligible unit may not receive more than 1 incentive payment under clause (i), regardless of\u2014 (I) the number of eligible units owned by the owner; or (II) the number of public housing agencies with which the owner has entered into housing assistance payment contracts. .\n##### (b) Security deposit payments\nSection 8(o) of the United States Housing Act of 1937 ( 42 U.S.C. 1437f(o) ), as amended by subsection (a), is amended by adding at the end the following:\n(24) Security deposit payments (A) Security deposit payment authority The Secretary shall provide assistance to public housing agencies to be used to pay the owner of a dwelling unit assisted under this subsection for a security deposit, or a substantial portion thereof, on behalf of the tenant of the dwelling unit in accordance with subparagraph (B). (B) Minimum PHA requirements A public housing agency that receives assistance from the Secretary under subparagraph (A) shall administer the assistance in accordance with the following conditions: (i) The public housing agency shall pay the owners of dwelling units assisted under this subsection for a security deposit, or a substantial portion thereof, in an amount determined by the public housing agency, on behalf of the tenants of the dwelling units. (ii) In making payments to owners of dwelling units under clause (i), the public housing agency shall give priority to owners of dwelling units occupied by extremely low-income families. (iii) The owner of a dwelling unit may deduct amounts from a security deposit payment received under clause (i) to cover damages beyond normal wear and tear caused by the tenant of the dwelling unit, any member of the tenant\u2019s household, or any guest or other person under the tenant\u2019s control. (iv) The public housing agency shall conduct a damage claims process whereby\u2014 (I) in order to deduct amounts from a security deposit payment received under clause (i), the owner of a covered dwelling unit must submit a claim to the public housing agency with an itemized list of damages and evidence and request reimbursement; and (II) the tenant of a covered dwelling unit may refute a claim submitted under subclause (I). (v) The public housing agency shall\u2014 (I) establish an amount of repair costs for which a tenant will be responsible; and (II) notify a tenant, upon the tenant entering into a lease for a dwelling unit assisted under this subsection, of the amount described in subclause (I). (vi) The public housing agency may determine what action to take if a tenant demonstrates an inability to pay the amount of repair costs for which the tenant is responsible under clause (v). (vii) At the end of a tenant's occupancy of a dwelling unit assisted under this subsection, the landlord shall return to the public housing agency any unused amount of a security deposit payment received under clause (i). (C) Rule of construction Nothing in subparagraph (B) shall be construed to prohibit a public housing agency from establishing additional conditions for the administration of assistance received under subparagraph (A) in accordance with applicable State and local laws. .\n##### (c) Landlord liaison bonus payments\nSection 8(o) of the United States Housing Act of 1937 ( 42 U.S.C. 1437f(o) ), as amended by subsection (b), is amended by adding at the end the following:\n(25) Landlord liaison bonus payments (A) In general Each year, the Secretary shall award 1 bonus payment to each public housing agency that employs, contracts with a service partner that employs, or demonstrates an intent to employ or contract with a service partner that employs, not less than 1 dedicated landlord liaison whose duties include, with respect to the tenant-based assistance program under subsection (o)\u2014 (i) conducting landlord outreach, recruitment, and retention; (ii) educating and training landlords regarding the program; and (iii) operating a phone hotline, online portal, monitored email address, or other mechanism designated by the Secretary for landlord questions and concerns regarding the program. (B) Demonstrating compliance The Secretary shall determine how a public housing agency may demonstrate that it offers or intends to offer a landlord liaison service for purposes of subparagraph (A). (C) Amount The Secretary shall establish an amount for the landlord liaison bonus payment authorized under subparagraph (A) that\u2014 (i) may vary by region; (ii) does not exceed the 150 percent of the average cost of employing, or contracting with a service partner that employs, such a landlord liaison, based on local market conditions; and (iii) is sufficient to incentivize public housing agencies to employ, or contact with a service partner that employs, such a landlord liaison. .\n##### (d) Housing Partnership Fund\nSection 8 of the United States Housing Act of 1937 ( 42 U.S.C. 1437f ) is amended by adding at the end the following:\n(ee) Herschel Lashkowitz Housing Partnership Fund (1) Establishment The Secretary shall establish a fund, to be known as the Herschel Lashkowitz Housing Partnership Fund , for the purpose of incentivizing landlords to participate in the tenant-based assistance program under subsection (o) in accordance with paragraph (2) of this subsection. (2) Authorized uses The Secretary shall use amounts from the Housing Partnership Fund for\u2014 (A) incentive payments under subsection (o)(23); (B) security deposit payments under subsection (o)(24); (C) landlord liaison bonus payments under subsection (o)(25); and (D) other uses, as determined by a public housing agency and approved by the Secretary, designed primarily\u2014 (i) to recruit owners of dwelling units, particularly dwelling units in census tracts with a poverty rate of less than 20 percent, to enter into housing assistance payment contracts under subsection (o); and (ii) to ensure that owners that enter into housing assistance payment contracts as described in clause (i) of this subparagraph continue to lease their dwelling units to tenants assisted under subsection (o). (3) Reports The Secretary shall require a public housing agency that receives assistance from the Herschel Lashkowitz Housing Partnership Fund to submit an annual report to the Secretary on the use of the assistance. (4) Authorization of additional appropriations There is authorized to be appropriated for deposit in the Herschel Lashkowitz Housing Partnership Fund $100,000,000 for each of fiscal years 2025 through 2029, to remain available until expended. .\n#### 6. Housing quality standards\n##### (a) Satisfaction of inspection requirements through participation in other housing programs\nSection 8(o)(8) of the United States Housing Act of 1937 ( 42 U.S.C. 1437f(o)(8) ), as amended by section 101(a) of the Housing Opportunity Through Modernization Act of 2016 ( Public Law 114\u2013201 ; 130 Stat. 783), is amended by adding at the end the following:\n(I) Satisfaction of inspection requirements through participation in other housing programs (i) Low-income housing tax credit-financed buildings A dwelling unit shall be deemed to meet the inspection requirements under this paragraph if\u2014 (I) the dwelling unit is in a building, the acquisition, rehabilitation, or construction of which was financed by a person who received a low-income housing tax credit under section 42 of the Internal Revenue Code of 1986 in exchange for that financing; (II) the dwelling unit was physically inspected and passed inspection as part of the low-income housing tax credit program described in subclause (I) during the preceding 12-month period; and (III) the applicable public housing agency is able to obtain the results of the inspection described in subclause (II). (ii) HOME Investment Partnerships Program A dwelling shall be deemed to meet the inspection requirements under this paragraph if\u2014 (I) the dwelling unit is assisted under the HOME Investment Partnerships Program under title II of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 12721 et seq. ); (II) the dwelling unit was physically inspected and passed inspection as part of the program described in subclause (I) during the preceding 12-month period; and (III) the applicable public housing agency is able to obtain the results of the inspection described in subclause (II). (iii) Rural Housing Service A dwelling unit shall be deemed to meet the inspection requirements under this paragraph if\u2014 (I) the dwelling unit is assisted by the Rural Housing Service of the Department of Agriculture; (II) the dwelling unit was physically inspected and passed inspection in connection with the assistance described in subclause (I) during the preceding 12-month period; and (III) the applicable public housing agency is able to obtain the results of the inspection described in subclause (II). (iv) Rule of construction Nothing in clause (i), (ii), or (iii) shall be construed to affect the operation of a housing program described in, or authorized under a provision of law described in, that clause. .\n##### (b) Pre-Approval of units\nSection 8(o)(8)(A) of the United States Housing Act of 1937 ( 42 U.S.C. 1437f(o)(8)(A) ) is amended by adding at the end the following:\n(iv) Initial inspection prior to lease agreement (I) Definition In this clause, the term new landlord means an owner of a dwelling unit who has not previously entered into a housing assistance payment contract with a public housing agency under this subsection for any dwelling unit. (II) Early inspection Upon the request of a new landlord, a public housing agency may inspect the dwelling unit owned by the new landlord to determine whether the unit meets the housing quality standards under subparagraph (B) before the unit is selected by a tenant assisted under this subsection. (III) Effect An inspection conducted under subclause (II) that determines that the dwelling unit meets the housing quality standards under subparagraph (B) shall satisfy this subparagraph and subparagraph (C) if the new landlord enters into a lease agreement with a tenant assisted under this subsection not later than 60 days after the date of the inspection. (IV) Information when family is selected When a public housing agency selects a family to participate in the tenant-based assistance program under this subsection, the public housing agency shall include in the information provided to the family a list of dwelling units that have been inspected under subclause (II) and determined to meet the housing quality standards under subparagraph (B). .\n#### 7. Small area fair market rent\n##### (a) Use of small area fair market rent\nSection 8(o)(1) of the United States Housing Act of 1937 ( 42 U.S.C. 1437f(o)(1) ) is amended by adding at the end the following:\n(F) Small area fair market rent (i) Definitions In this subparagraph\u2014 (I) the term metropolitan area means a metropolitan statistical area, as defined by the Office of Management and Budget; and (II) the term small area fair market rent means the fair market rent established for a ZIP Code area within a metropolitan area. (ii) Use of small area fair market rent Notwithstanding subsection (c) or any other provision of this subsection, not later than 3 years after the date of enactment of this subparagraph, the Secretary shall designate a number of metropolitan areas in which public housing agencies are required to use the small area fair market rent to determine the fair market rental for dwelling units for purposes of tenant-based assistance under this subsection that is not less than 3 times the number of metropolitan areas so designated in the final rule of the Secretary entitled Establishing a More Effective Fair Market Rent System; Using Small Area Fair Market Rents in the Housing Choice Voucher Program Instead of the Current 50th Percentile FMRs , published in the Federal Register on November 16, 2016 (81 Fed. Reg. 80567). (iii) Hold harmless If the application of clause (ii) would cause a decrease in the payment standard used to calculate the amount of tenant-based assistance provided to a family under this subsection, a public housing agency shall continue to use the existing higher payment standard to calculate the amount of such assistance for the family for as long as the family continues to receive such assistance in the same dwelling unit. .\n##### (b) Conforming amendment\nSection 8(o)(1)(B) of the United States Housing Act of 1937 ( 42 U.S.C. 1437f(o)(1)(B) ) is amended by inserting after subsection (c) the following: (subject to subparagraph (F) of this paragraph) .\n#### 8. Section 8 Management Assessment Program\n##### (a) Definition\nIn this section, the term Section 8 Management Assessment Program means the program set forth in part 985 of title 24, Code of Federal Regulations (or any successor regulation).\n##### (b) Deconcentration of participating dwelling units\nThe Secretary shall explore ways to reform and modernize the Section 8 Management Assessment Program to assess public housing agencies in a manner that promotes\u2014\n**(1)**\npositive interactions with landlords, including timely payment of rent and identification of the dwelling unit for which a subsidy payment is being made; and\n**(2)**\nan increase in the diversity of areas where dwelling units are leased to support voucher holders who want to access to low-poverty, integrated neighborhoods.\n##### (c) Rule of construction\nNothing in subsection (b) shall be construed to prevent the Secretary from\u2014\n**(1)**\nreforming the Section 8 Management Assessment Program to assess public housing agencies in other areas of performance; or\n**(2)**\nreforming the Section 8 Management Assessment Program in any other manner, at the discretion of the Secretary.\n#### 9. Annual report on effectiveness of Act\n##### (a) Definitions\nIn this section\u2014\n**(1)**\nthe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Banking, Housing, and Urban Affairs of the Senate;\n**(B)**\nthe Subcommittee on Transportation, Housing and Urban Development, and Related Agencies of the Committee on Appropriations of the Senate;\n**(C)**\nthe Committee on Financial Services of the House of Representatives; and\n**(D)**\nthe Subcommittee on Transportation, Housing and Urban Development, and Related Agencies of the Committee on Appropriations of the House of Representatives; and\n**(2)**\nthe term high-opportunity area \u2014\n**(A)**\nshall be defined by the Secretary for purposes of this section; and\n**(B)**\ndoes not include any census tract in which the poverty rate is equal to or greater than 20 percent.\n##### (b) Report\nNot later than 1 year after the date of enactment of this Act, and annually thereafter for 5 total years, the Secretary shall submit to the appropriate congressional committees and make publicly available a report that\u2014\n**(1)**\nevaluates the effectiveness of this Act and the amendments made by this Act in recruiting and retaining landlords who accept vouchers under the Housing Choice Voucher program, particularly landlords with dwelling units in high-opportunity neighborhoods; and\n**(2)**\nincludes\u2014\n**(A)**\nthe number of landlords in the United States who accept housing choice vouchers under the Housing Choice Voucher program and the number of dwelling units assisted under the Housing Choice Voucher program;\n**(B)**\nany net changes to the number of landlords or dwelling units described in subparagraph (A) during the preceding year;\n**(C)**\nthe number of landlords described in subparagraph (A) who own disability-accessible dwelling units assisted under the Housing Choice Voucher program and the number of those dwelling units; and\n**(D)**\nthe number of landlords described in subparagraph (A) who own dwelling units assisted under the Housing Choice Voucher program in high-opportunity areas and the number of those dwelling units.",
      "versionDate": "2025-03-10",
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
        "actionDate": "2025-03-06",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "890",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Choice in Affordable Housing Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional oversight",
            "updateDate": "2025-07-22T13:09:34Z"
          },
          {
            "name": "Disability and paralysis",
            "updateDate": "2025-07-22T13:09:34Z"
          },
          {
            "name": "Housing and community development funding",
            "updateDate": "2025-07-22T13:09:34Z"
          },
          {
            "name": "Housing industry and standards",
            "updateDate": "2025-07-22T13:09:34Z"
          },
          {
            "name": "Indian social and development programs",
            "updateDate": "2025-07-22T13:09:34Z"
          },
          {
            "name": "Landlord and tenant",
            "updateDate": "2025-07-22T13:09:34Z"
          },
          {
            "name": "Public housing",
            "updateDate": "2025-07-22T13:09:34Z"
          },
          {
            "name": "Veterans' loans, housing, homeless programs",
            "updateDate": "2025-07-22T13:09:34Z"
          }
        ]
      },
      "policyArea": {
        "name": "Housing and Community Development",
        "updateDate": "2025-03-26T12:40:34Z"
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
      "date": "2025-03-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1981ih.xml"
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
      "title": "Choice in Affordable Housing Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-25T07:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Choice in Affordable Housing Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-25T07:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To increase the number of landlords participating in the Housing Choice Voucher program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-25T07:33:30Z"
    }
  ]
}
```
