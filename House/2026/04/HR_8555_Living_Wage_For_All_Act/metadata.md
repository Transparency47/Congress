# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8555?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8555
- Title: Living Wage For All Act
- Congress: 119
- Bill type: HR
- Bill number: 8555
- Origin chamber: House
- Introduced date: 2026-04-28
- Update date: 2026-05-20T19:14:09Z
- Update date including text: 2026-05-20T19:14:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-28: Introduced in House
- 2026-04-28 - IntroReferral: Introduced in House
- 2026-04-28 - IntroReferral: Introduced in House
- 2026-04-28 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2026-04-28: Introduced in House

## Actions

- 2026-04-28 - IntroReferral: Introduced in House
- 2026-04-28 - IntroReferral: Introduced in House
- 2026-04-28 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-28",
    "latestAction": {
      "actionDate": "2026-04-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8555",
    "number": "8555",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "R000617",
        "district": "3",
        "firstName": "Delia",
        "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
        "lastName": "Ramirez",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Living Wage For All Act",
    "type": "HR",
    "updateDate": "2026-05-20T19:14:09Z",
    "updateDateIncludingText": "2026-05-20T19:14:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-28",
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
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-28",
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
          "date": "2026-04-28T13:04:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "IL"
    },
    {
      "bioguideId": "M001246",
      "district": "11",
      "firstName": "Analilia",
      "fullName": "Rep. Mejia, Analilia [D-NJ-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Mejia",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "NJ"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "CA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "MI"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "NJ"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "MI"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "NY"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "AZ"
    },
    {
      "bioguideId": "G000606",
      "district": "7",
      "firstName": "Adelita",
      "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Grijalva",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "AZ"
    },
    {
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "NY"
    },
    {
      "bioguideId": "C001131",
      "district": "35",
      "firstName": "Greg",
      "fullName": "Rep. Casar, Greg [D-TX-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Casar",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "TX"
    },
    {
      "bioguideId": "W000808",
      "district": "24",
      "firstName": "Frederica",
      "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "FL"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
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
      "sponsorshipDate": "2026-04-28",
      "state": "DC"
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
      "sponsorshipDate": "2026-04-28",
      "state": "IL"
    },
    {
      "bioguideId": "E000297",
      "district": "13",
      "firstName": "Adriano",
      "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Espaillat",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "NY"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "HI"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "NM"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "WA"
    },
    {
      "bioguideId": "N000188",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Norcross, Donald [D-NJ-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Norcross",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "NJ"
    },
    {
      "bioguideId": "M001245",
      "district": "18",
      "firstName": "Christian",
      "fullName": "Rep. Menefee, Christian D. [D-TX-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Menefee",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "TX"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "IL"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "CA"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "NJ"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "MS"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-05-04",
      "state": "PA"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2026-05-04",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8555ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8555\nIN THE HOUSE OF REPRESENTATIVES\nApril 28, 2026 Mrs. Ramirez (for herself, Mr. Garc\u00eda of Illinois , Ms. Mejia , Ms. Simon , Mr. Thanedar , Mrs. Watson Coleman , Ms. Tlaib , Mr. Goldman of New York , Ms. Ansari , Mrs. Grijalva , Ms. Vel\u00e1zquez , Mr. Casar , Ms. Wilson of Florida , Mr. Khanna , Ms. Norton , Mr. Jackson of Illinois , Mr. Espaillat , Ms. Tokuda , Ms. Stansbury , Ms. Jayapal , Mr. Norcross , Mr. Menefee , Mr. Davis of Illinois , Mr. Lieu , Mrs. McIver , and Mr. Thompson of Mississippi ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo place the Federal minimum wage on a durable path toward a living wage aligned with the national median wage, to require large, highly profitable corporations to lead the transition, to end all subminimum wages, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Living Wage For All Act .\n#### 2. Findings and purpose\n##### (a) Findings\nCongress finds the following:\n**(1)**\nIt is a national priority that work pays a living wage to all workers, and that the Federal minimum wage be aligned with the actual cost of living. The wage increases established by this Act\u2014including the attainment of a $25 hourly wage\u2014are steps toward that goal and shall be followed by continued adjustments to ensure that the minimum wage remains responsive to changes in wages and economic conditions over time.\n**(2)**\nBased on the best available data, including wage data from the Bureau of Labor Statistics and economic projections from the Congressional Budget Office, a minimum wage of at least $25 per hour represents a conservative baseline step toward aligning wages with the cost of living nationwide.\n**(3)**\nLarge, highly profitable corporations have the greatest capacity to raise wages and should therefore lead the transition to higher wage standards before smaller employers.\n**(4)**\nTying the Federal minimum wage to a fixed share of the national median hourly wage ensures that wage standards rise with the economy and prevents future erosion of purchasing power.\n**(5)**\nA Federal minimum wage aligned with median wages strengthens economic security, reduces reliance on public assistance, and promotes broad-based economic growth.\n##### (b) Purpose\nThe purpose of this Act is to place the Federal minimum wage on a durable path toward a living wage by ensuring that it reaches a level equal to two-thirds of the national median hourly wage, consistent with the phase-in schedule and median-wage adjustments established under this Act, as soon as economically possible, and remains indexed to that standard thereafter, while requiring large corporations to lead the transition and providing additional adjustment time for other employers.\n#### 3. Definitions\nIn this Act:\n**(1) Large employer**\nThe term large employer means any employer that\u2014\n**(A)**\nhas annual gross revenues of $1,000,000,000 or more; or\n**(B)**\nemploys 500 or more employees nationwide; as determined by the Secretary of Labor.\n**(2) Other employer**\nThe term other employer means any employer that does not meet the definition of a large employer.\n#### 4. Minimum wage increases\n##### (a) In general\nSection 6(a)(1) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 206(a)(1) ) is amended to read as follows:\n(1) Minimum wage Except as otherwise provided in this section, not less than\u2014 (A) Large employers Each employer that is a large employer shall pay each employee wages at a rate not less than\u2014 (i) $12.00 per hour, beginning January 1, 2026; (ii) $15.00 per hour, beginning January 1, 2027; (iii) $18.00 per hour, beginning January 1, 2028; (iv) $20.00 per hour, beginning January 1, 2029; (v) $22.50 per hour, beginning January 1, 2030; and (vi) $25.00 per hour, beginning January 1, 2031, subject to subsection (h): Provided , That, notwithstanding the preceding schedule, the wage required under this subparagraph shall not exceed the wage determined under subsection (h) for the applicable year. (B) Other employers Each employer that is an other employer shall pay each employee wages at a rate not less than\u2014 (i) $12.00 per hour, beginning January 1, 2026; (ii) $14.00 per hour, beginning January 1, 2027; (iii) $16.00 per hour, beginning January 1, 2028; (iv) $18.00 per hour, beginning January 1, 2029; (v) $20.00 per hour, beginning January 1, 2030; (vi) $20.60 per hour, beginning January 1, 2031; (vii) $21.20 per hour, beginning January 1, 2032; (viii) $21.80 per hour, beginning January 1, 2033; (ix) $22.40 per hour, beginning January 1, 2034; (x) $23.00 per hour, beginning January 1, 2035; (xi) $23.60 per hour, beginning January 1, 2036; (xii) $24.20 per hour, beginning January 1, 2037; and (xiii) $25.00 per hour, beginning January 1, 2038, subject to subsection (h). .\n#### 5. Median wage standard and indexing\nSection 6 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 206 ) is amended by adding at the end the following:\n(h) Determination based on the national median hourly wage (1) Target standard The minimum wage shall be equal to two-thirds of the national median hourly wage of all employees, as determined by the Bureau of Labor Statistics. (2) Phase-in alignment During the phase-in period described in subsection (a)(1), as applicable to the employer\u2014 (A) if the scheduled minimum wage for a calendar year under subsection (a)(1)(A) or (a)(1)(B) would exceed two-thirds of the national median hourly wage for that year, the minimum wage shall be set at two-thirds of the national median hourly wage for that year; and (B) if, at the conclusion of the applicable phase-in schedule, the minimum wage has not yet reached two-thirds of the national median hourly wage, the minimum wage shall continue to increase annually by the lesser of\u2014 (i) $1.00; or (ii) the amount necessary to reach two-thirds of the national median hourly wage. (3) Indexing after attainment Once the minimum wage equals two-thirds of the national median hourly wage, it shall thereafter be automatically adjusted each year to maintain that ratio. (4) Data and projections In carrying out this subsection, the Secretary shall rely on\u2014 (A) actual median wage data published by the Bureau of Labor Statistics; and (B) where necessary during the phase-in period, including for purposes of estimating two-thirds of the national median hourly wage during the phase-in period, economic projections from the Congressional Budget Office or successor agencies. (5) Publication Each annual determination under this subsection shall be published not later than 90 days before its effective date. .\n#### 6. Tipped employees\n##### (a) Base minimum wage for tipped employees and tips retained by employees\nSection 3(m)(2)(A)(i) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203(m)(2)(A)(i) ) is amended to read as follows:\n(i) the cash wage paid such employee, which for purposes of such determination shall be not less than\u2014 (I) for tipped employees of large employers (as defined in section 3 of the Living Wage For All Act), not less than\u2014 (aa) $6.00 an hour, for the 1-year period beginning on the effective date under section 11 of the Living Wage For All Act; (bb) $9.00 an hour, beginning 1 year after such effective date; (cc) $12.00 an hour, beginning 2 years after such effective date; (dd) $15.00 an hour, beginning 3 years after such effective date; (ee) $18.00 an hour, beginning 4 years after such effective date; and (ff) beginning 5 years after such effective date, the minimum wage in effect under section 6(a)(1) for such employee; and (II) for tipped employees of other employers (as defined in section 3 of the Living Wage For All Act), not less than\u2014 (aa) $4.75 an hour, for the 1-year period beginning on the effective date under section 11 of the Living Wage For All Act; (bb) for each succeeding 1-year period until the cash wage under this subclause equals the minimum wage in effect under section 6(a)(1) for such employee, an hourly wage equal to the amount determined under this subclause for the preceding year, increased by the lesser of\u2014 (AA) $1.75; or (BB) the amount necessary for the wage under this subclause to equal the minimum wage in effect under section 6(a)(1) for such employee; and (cc) for each succeeding 1-year period after the increase made pursuant to subclause (II)(bb), the minimum wage in effect under section 6(a)(1) for such employee; and .\n##### (b) Tips retained by employees\nSection 3(m)(2)(A) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203(m)(2)(A) ) is amended\u2014\n**(1)**\nin the second sentence of the matter following clause (ii), by striking of this subsection, and all tips received by such employee have been retained by the employee and inserting of this subsection. Any employee shall have the right to retain any tips received by such employee ; and\n**(2)**\nby adding at the end the following: An employer shall inform each employee of the right and exception provided under the preceding sentence. .\n##### (c) Scheduled repeal of separate minimum wage for tipped employees\n**(1) Tipped employees**\nSection 3(m)(2)(A) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203(m)(2)(A) ), as amended by subsections (a) and (b), is further amended by striking the sentence beginning with In determining the wage an employer is required to pay a tipped employee, and all that follows through of this subsection. and inserting The wage required to be paid to a tipped employee shall be the wage set forth in section 6(a)(1). .\n**(2) Publication of notice**\nSubsection (i) of section 6 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 206 ), as added by section 8 of the Living Wage For All Act, is amended by striking or in accordance with subclause (II) or (III) of section 3(m)(2)(A)(i), and inserting or in accordance with section 3(m)(2)(A)(i), .\n**(3) Effective date**\nThe amendments made by paragraphs (1) and (2) shall take effect, with respect to a tipped employee, on the date that is 1 day after the date on which the cash wage required under section 3(m)(2)(A)(i) equals the minimum wage in effect under section 6(a)(1) for such employee.\n##### (d) Penalties\nSection 16 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 216 ) is amended\u2014\n**(1)**\nin the third sentence of subsection (b), by inserting or used after kept ; and\n**(2)**\nin the second sentence of subsection (e)(2), by inserting or used after kept .\n#### 7. Youth workers\n##### (a) Base minimum wage for newly hired employees who are less than 20 years old\nSection 6(g)(1) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 206(g)(1) ) is amended by striking a wage which is not less than $4.25 an hour. and inserting the following:\na wage at a rate that is not less than\u2014 (A) for the 1-year period beginning on the effective date under section 11 of the Living Wage For All Act, $6.00 an hour; (B) for each succeeding 1-year period until the hourly wage under this paragraph equals the wage in effect under section 6(a)(1) for such period, an hourly wage equal to the amount determined under this paragraph for the preceding year, increased by the lesser of\u2014 (i) $1.75; or (ii) the amount necessary for the wage in effect under this paragraph to equal the wage in effect under section 6(a)(1) for such period; and (C) for each succeeding 1-year period after the increase made pursuant to subparagraph (B)(ii), the minimum wage in effect under section 6(a)(1). .\n##### (b) Scheduled repeal of separate minimum wage for newly hired employees who are less than 20 years old\n**(1) In general**\nSection 6(g) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 206(g) ), as amended by subsection (a), shall be repealed.\n**(2) Publication of notice**\nSubsection (i) of section 6 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 206 ), as added by section 8 of the Living Wage For All Act, is amended by striking or subparagraph (B) or (C) of subsection (g)(1) and inserting or subsection (g)(1) .\n**(3) Effective date**\nThe repeal and amendment made by paragraphs (1) and (2), respectively, shall take effect on the date that is 1 day after the date on which the hourly wage under section 6(g)(1) equals the minimum wage in effect under section 6(a)(1).\n#### 8. Publication of notice\nSection 6 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 206 ), as amended by this Act, is further amended by adding at the end the following:\n(i) Not later than 60 days prior to the effective date of any increase in the required wage determined under subsection (a)(1) or subsection (g)(1), or in accordance with section 3(m)(2)(A)(i) or section 14(c)(1)(A), the Secretary shall publish in the Federal Register and on the website of the Department of Labor a notice announcing each increase in such required wage. .\n#### 9. Workers with disabilities\n##### (a) Wages\n**(1) Transition to living wages for individuals with disabilities**\nSubparagraph (A) of section 14(c)(1) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 214(c)(1) ) is amended to read as follows:\n(A) at a rate that equals or exceeds, for each year, the greater of\u2014 (i) (I) $5.00 an hour, for the 1-year period beginning on the effective date under section 11 of the Living Wage For All Act; (II) for each succeeding 1-year period until the wage rate under this clause equals the wage rate in effect under section 6(a)(1) for such period, an hourly wage equal to the amount determined under this clause for the preceding year, increased by the lesser of\u2014 (aa) $1.75; or (bb) the amount necessary for the wage rate under this clause to equal the wage rate in effect under section 6(a)(1) for such period; and (III) for each succeeding 1-year period after the increase made pursuant to clause (II)(bb), the wage rate in effect under section 6(a)(1); or (ii) if applicable, the wage rate in effect on the day before the date of enactment of the Living Wage For All Act for the employment, under a special certificate issued under this paragraph, of the individual for whom the wage rate is being determined under this subparagraph, .\n**(2) Prohibition on new special certificates; transition assistance**\n**(A) In general**\nSection 14(c) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 214(c) ) is amended by adding at the end the following:\n(6) Prohibition on new special certificates Notwithstanding paragraph (1), the Secretary shall not issue a special certificate under this subsection to an employer that was not issued a special certificate under this subsection before the date of enactment of the Living Wage For All Act. (7) Transition assistance Upon request, the Secretary shall provide\u2014 (A) technical assistance and information to employers issued a special certificate under this subsection for the purposes of\u2014 (i) assisting such employers to comply with this subsection, as amended by the Living Wage For All Act; and (ii) ensuring continuing employment opportunities for individuals with disabilities receiving a special minimum wage rate under this subsection; and (B) information to individuals employed at a special minimum wage rate under this subsection, which may include referrals to Federal or State entities with expertise in competitive integrated employment. .\n**(B) Effective date**\nThe amendments made by this paragraph shall take effect on the date of enactment of this Act.\n**(3) Sunset**\nSection 14(c) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 214(c) ), as amended by paragraph (2), is further amended by adding at the end the following:\n(8) Sunset Beginning on the day after the date on which the wage rate described in paragraph (1)(A)(i) first equals the wage rate in effect under section 6(a)(1), the authority to issue special certificates under paragraph (1) shall expire, and no special certificates issued under paragraph (1) shall have any legal effect. .\n##### (b) Publication of notice\n**(1) Amendment**\nSubsection (i) of section 6 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 206 ), as added by section 8 of the Living Wage For All Act, is amended by striking or section 14(c)(1)(A) .\n**(2) Effective date**\nThe amendment made by paragraph (1) shall take effect on the day after the date on which the wage rate described in section 14(c)(1)(A)(i) first equals the wage rate in effect under section 6(a)(1).\n#### 10. Incarcerated workers\nSection 3 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203 ) is amended\u2014\n**(1)**\nin subsection (e)\u2014\n**(A)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (B), by striking ; and and inserting a semicolon;\n**(ii)**\nin subparagraph (C)(ii)(V), by striking the period at the end and inserting ; and ; and\n**(iii)**\nby adding at the end the following:\n(D) any individual employed as an incarcerated worker by a public agency that operates the correctional facility in which such individual is incarcerated or detained. ; and\n**(B)**\nby adding at the end the following:\n(6) The term employee includes (in addition to an individual described in paragraph (2)(D)) any individual employed as an incarcerated worker by a private entity that operates, through a contract with a public agency, the correctional facility in which such individual is incarcerated or detained. ;\n**(2)**\nin subsection (m)(1), by striking any employee. and inserting any employee: Provided further , That, in the case of an employee who is an incarcerated worker, the cost of board, lodging, or other facilities and any amount taken from amounts paid such incarcerated worker for payment of a court-imposed fee shall not be included in the wage paid to such employee. ; and\n**(3)**\nby adding at the end the following:\n(z) (1) Incarcerated worker means an individual, incarcerated or detained in a correctional facility operated by a public agency or by a private entity through a contract with a public agency, who performs work offered or required by or through the correctional facility, including work associated with prison work programs, work release programs, the UNICOR program, State prison industries, public works programs, restitution centers, correctional facility operations and maintenance, and private entities. (2) An incarcerated worker shall be considered employed by\u2014 (A) the public agency operating the correctional facility in which the individual is incarcerated or detained; or (B) in the case of a correctional facility operated by a private entity through a contract with a public agency, such private entity. (aa) Correctional facility has the meaning given such term in section 901 of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10251 ). (bb) (1) Court-imposed fee means any fee imposed by a court as a result of a criminal conviction, including any surcharge imposed for a felony or misdemeanor conviction, a criminal justice administrative fee, a court-appointed attorney fee, a court clerk fee, a filing clerk fee, a DNA database fee, a jury fee, a crime lab analysis fee, a late fee, an installment fee, or any other court cost. (2) The term \u2018court-imposed fee\u2019 does not include any amount required by a court to be paid for child support, to a crime victim compensation fund, for a civil judgment, or for a criminal fine. .\n#### 11. Effective date\nExcept as otherwise provided, this Act and the amendments made by this Act shall take effect on the first day of the calendar year that begins after the date of enactment of this Act.",
      "versionDate": "2026-04-28",
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
        "name": "Labor and Employment",
        "updateDate": "2026-05-20T19:14:08Z"
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
      "date": "2026-04-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8555ih.xml"
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
      "title": "Living Wage For All Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-08T05:53:34Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Living Wage For All Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-08T05:53:33Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To place the Federal minimum wage on a durable path toward a living wage aligned with the national median wage, to require large, highly profitable corporations to lead the transition, to end all subminimum wages, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-08T05:48:42Z"
    }
  ]
}
```
