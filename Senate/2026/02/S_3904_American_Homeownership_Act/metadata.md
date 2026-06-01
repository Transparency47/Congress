# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3904?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3904
- Title: American Homeownership Act
- Congress: 119
- Bill type: S
- Bill number: 3904
- Origin chamber: Senate
- Introduced date: 2026-02-24
- Update date: 2026-03-13T22:31:13Z
- Update date including text: 2026-03-13T22:31:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-24: Introduced in Senate
- 2026-02-24 - IntroReferral: Introduced in Senate
- 2026-02-24 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-02-24: Introduced in Senate

## Actions

- 2026-02-24 - IntroReferral: Introduced in Senate
- 2026-02-24 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-24",
    "latestAction": {
      "actionDate": "2026-02-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3904",
    "number": "3904",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "W000817",
        "district": "",
        "firstName": "Elizabeth",
        "fullName": "Sen. Warren, Elizabeth [D-MA]",
        "lastName": "Warren",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "American Homeownership Act",
    "type": "S",
    "updateDate": "2026-03-13T22:31:13Z",
    "updateDateIncludingText": "2026-03-13T22:31:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-24",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-02-24",
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
          "date": "2026-02-24T21:33:24Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "OR"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "MN"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "MN"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "CT"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "IL"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "IL"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "NM"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "HI"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "VA"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "NJ"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "MA"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "CT"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "HI"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2026-02-24",
      "state": "VT"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "CA"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "MD"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "VT"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "NJ"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "DE"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3904is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3904\nIN THE SENATE OF THE UNITED STATES\nFebruary 24, 2026 Ms. Warren (for herself, Mr. Merkley , Ms. Klobuchar , Ms. Smith , Mr. Blumenthal , Ms. Duckworth , Mr. Durbin , Mr. Heinrich , Ms. Hirono , Mr. Kaine , Mr. Kim , Mr. Markey , Mr. Murphy , Mr. Schatz , Mr. Sanders , Mr. Schiff , Mr. Van Hollen , Mr. Welch , and Mr. Booker ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to deny interest and depreciation deductions for certain taxpayers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the American Homeownership Act .\n#### 2. Disallowance of deduction for interest paid on real property owned by certain real property owners\n##### (a) In general\nSection 163 of the Internal Revenue Code of 1986 is amended by redesignating subsection (n) as subsection (o) and by inserting after subsection (m) the following new subsection:\n(n) Interest paid on residential rental property owned by certain real property owners (1) In general No deduction shall be allowed under this chapter for any interest paid or accrued in connection with\u2014 (A) any applicable residential property in which an institutional investment entity (directly or indirectly) holds a majority interest, or (B) single-family residential property in which a large owner (directly or indirectly) holds a majority interest. (2) Exception for sales to individuals or qualified nonprofit organizations (A) In general Paragraph (1) shall not apply with respect to interest paid or accrued in the taxable year in which applicable residential property is sold. (B) Exception Subparagraph (A) shall not apply unless the sale described in such subparagraph is\u2014 (i) a sale to an individual for use as the principle residence of the individual (within the meaning of section 121), or (ii) a sale to any qualified nonprofit organization. (C) Qualified nonprofit organization (i) In general For purposes of this paragraph, the term qualified nonprofit organization means any organization which\u2014 (I) is not organized for profit, and (II) has as a principal purpose the creation, development, or preservation of affordable housing. (ii) Certain organizations included The term qualified nonprofit organization shall include\u2014 (I) any community development corporation (as defined in section 204(b) of the Department of Veterans Affairs and Housing and Urban Development, and Independent Agencies Appropriations Act, 1997 (12 U.S.C. 1715z\u201311a(b))), (II) any community housing development organization (as defined in section 104 of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 12704 )), (III) any community-based development organization qualified under section 570.204 of title 24, Code of Federal Regulations, as in effect on the date of the enactment of this subsection, (IV) any land bank, (V) any resident-owned cooperative or community land trust, and (VI) any subsidiary of a public housing agency (as defined in section 3(b)(6) of the United States Housing Act of 1937 ( 42 U.S.C. 1437a(b)(6) )). (iii) Land bank For purposes of this subparagraph, the term land bank means a government entity, agency, or program, or a special purpose nonprofit entity formed by one or more units of government in accordance with State or local land bank enabling law, that has been designated by one or more State or local governments to acquire, steward, and dispose of vacant, abandoned, or other problem properties in accordance with locally determined priorities and goals. (iv) Community land trust For purposes of this subparagraph, the term community land trust means a nonprofit entity, a State, a unit of local government, or an instrumentality of a State or unit of local government that\u2014 (I) is not managed by, or an affiliate of, a for-profit organization, (II) has as a primary purpose of acquiring, developing, or holding land to provide housing that is permanently affordable to low- and moderate-income persons, (III) monitors properties to ensure affordability is preserved, (IV) provides housing that is permanently affordable to low- and moderate-income persons using a ground lease, deed covenant, or other similar legally enforceable measure, determined acceptable by the Secretary, that\u2014 (aa) keeps housing affordable to low- and moderate-income persons for not less than 30 years, and (bb) enables low- and moderate-income persons to rent or purchase the housing for homeownership, and (V) maintains preemptive purchase options to purchase the property if such purchase would allow the housing to remain affordable to low- and moderate-income persons. (3) Exception for new single-family housing (A) In general In the case of a single-family residential property the original use of which begins with an eligible taxpayer after December 31, 2023, paragraph (1) shall not apply to interest paid or accrued by such eligible taxpayer with respect to such property in any taxable year during the 5-taxable-year period beginning with the taxable year in which property is placed in service. (B) Eligible taxpayer For purposes of this paragraph, the term eligible taxpayer means the person who constructed the single-family residential property. (4) Exception for new multi-family housing (A) In general Paragraph (1) shall not apply to any multi-family residential property the original use of which begins with an eligible taxpayer after December 31, 2023. (B) Eligible taxpayer For purposes of this paragraph, the term eligible taxpayer means the person who constructed the multi-family residential property. (C) Multi-family residential property For purposes of this paragraph, the term multi-family residential property means any applicable residential property which has 5 or more dwelling units (as defined in section 168(e)(2)(A)(ii)(I)). (5) Exception to preserve uninhabitable housing (A) In general In the case of any interest paid or accrued with respect to debt which is incurred for the primary purpose of substantially rehabilitating previously uninhabitable applicable residential property, paragraph (1) shall not apply to interest paid or accrued in any taxable year during the 5-taxable-year period beginning with taxable year in which such debt is originally paid or accrued. (B) Uninhabitable For purposes of this paragraph, the term uninhabitable means, with respect to applicable residential property, property that is not fit for human occupancy, contains serious defects posing risks to health or safety, or does not meet structural or core system elements of local building codes. (C) Substantial rehabilitation For purposes of this paragraph, the term substantial rehabilitation means, with respect to applicable residential property, structural repairs or rebuilding, with the cost of rehabilitation generally being a significant portion of the property\u2019s value after the work is completed. (6) Exception for affordable housing Paragraph (1) shall not apply to any interest paid or accrued with respect to any property\u2014 (A) which is Federally assisted housing (as defined in section 579 of the Quality Housing and Work Responsibility Act of 1998), or (B) (i) which\u2014 (I) has received an allocation of housing credit dollar amount under section 42(h) for such taxable year or any prior taxable year, or (II) is a building described in section 42(h)(4)(B), and (ii) for which an extended low-income housing commitment described in section 42(h)(6) is in effect as of the end of the taxable year. (7) Definitions For purposes of this subsection\u2014 (A) Institutional investment entity The term Institutional investment entity means\u2014 (i) any issuer that is exempt from registration under section 3(c) of the Investment Company Act of 1940, or (ii) any other investment vehicle that pools funds exclusively from accredited investors as defined in section 230.501 of title 17, Code of Federal Regulations (or any successor regulation). (B) Large owner (i) In general For purposes of this subsection, the term large owner means any person who (directly or indirectly) holds a majority interest in single-family residential rental properties which in the aggregate contain 50 or more dwelling units. (ii) Aggregation rules For purposes of this subparagraph, all persons treated as a single employer under subsection (a) or (b) of section 52, or subsection (m) or (o) of section 414, shall be treated as one taxpayer for purposes of this section. (iii) Modifications (I) In general For purposes of applying clause (ii)\u2014 (aa) section 52(a) shall be applied by substituting component members for members , and (bb) for purposes of applying section 52(b), the term trade or business shall include any activity treated as a trade or business under paragraph (5) or (6) of section 469(c) (determined without regard to the phrase To the extent provided in regulations in such paragraph (6)). (II) Component member For purposes of this subparagraph, the term component member has the meaning given such term by section 1563(b), except that the determination shall be made without regard to subparagraphs (B), (C), (D) or (E) of paragraph (2) thereof. (III) No inference The modifications made by subclause (I) shall not be construed to create any inference with respect to the proper application of section 52 with respect to any other provision of this title. (C) Applicable residential property (i) In general The term applicable residential property means any property which is\u2014 (I) residential rental property (as defined in section 168(e)(2)(A)(i)), (II) a manufactured housing community, or (III) a manufactured home (as defined in section 603 of the National Manufactured Housing Construction and Safety Standards Act of 1974 ( 42 U.S.C. 5402 )) which is not residential rental property (as so defined). (ii) Manufactured housing community The term manufactured housing community means a residential real estate development with lots on which factory-built homes, including manufactured homes, are located, together with supporting infrastructure. (D) Single-family residential property The term single-family residential property means any applicable residential property which contains 4 or fewer dwelling units (as defined in section 168(e)(2)(A)(ii)(I)). (8) Regulations The Secretary shall prescribe such regulations as may be necessary or appropriate to carry out the purposes of this subsection, including\u2014 (A) regulations for identifying the amount of interest paid or accrued in connection with applicable residential property and single-family residential property, including any interest paid or accrued through indirect financing arrangements, (B) regulations, in consultation with the Secretary of Housing and Urban Development, for identifying and, to the extent provided by the Secretary, substantiating the amount of interest paid or accrued with respect to debt which is incurred for the primary purpose of substantially rehabilitating previously uninhabitable applicable residential property under paragraph (5), and (C) regulations to prevent the avoidance of the purposes of this subsection. .\n##### (b) Application to capitalized amounts\n**(1) In general**\nSection 263A(f)(2) of the Internal Revenue Code of 1986 is amended by adding at the end the following new subparagraph:\n(D) Exception for certain interest of certain real property owners Subparagraph (A) shall not apply to any interest for which a deduction would be disallowed under section 163(n). .\n**(2) Carrying charges**\nSection 266 of such Code is amended\u2014\n**(A)**\nby striking No deduction and inserting the following:\n(a) In general No deduction , and\n**(B)**\nby adding at the end the following new subsection:\n(b) Special rule for certain interest of certain real property owners No election may be made under this section to treat as chargeable to capital account any interest for which a deduction would be disallowed under section 163(n). .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this Act.\n#### 3. Disallowance of depreciation in connection with property of certain real property owners\n##### (a) In general\nSection 167 of the Internal Revenue Code of 1986 is amended by redesignating subsection (i) as subsection (j) and by inserting after subsection (h) the following new subsection:\n(i) Deduction disallowed for certain real property owners (1) In general No deduction shall be allowed under this section for\u2014 (A) any applicable residential property in which an institutional investment entity (directly or indirectly) holds a majority interest, or (B) single-family residential property in which a large owner (directly or indirectly) holds a majority interest. (2) Exceptions Rules similar to the rules of paragraphs (2), (3), (4), (5), and (6) of section 163(n) shall apply for purposes of this subsection. (3) Definitions For purposes of this subsection\u2014 (A) Applicable residential property The term applicable residential property means\u2014 (i) any property described in section 163(n)(7)(C), and (ii) any improvements to real property which\u2014 (I) are directly related to dwelling units contained on property described in clause (i), and (II) are located on the site of such dwelling units. (B) Single-family residential property The term single-family residential property means\u2014 (i) any property described in section 163(n)(7)(D), and (ii) any improvements to real property which\u2014 (I) are directly related to dwelling units contained on property described in clause (i), and (II) are located on the site of such dwelling units. (C) Institutional investment entity; large owner The terms institutional investment entity and large owner have the respective meanings given such terms under section 163(n). (4) Regulations The Secretary shall prescribe such regulations as may be necessary or appropriate to carry out the purposes of this subsection, including regulations to prevent the avoidance of the purposes of this subsection. .\n##### (b) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this Act.\n#### 4. Prohibition on sale or provision of Federally backed mortgage loans to certain investors\n##### (a) Definitions\nIn this section:\n**(1) Covered entity**\nThe term covered entity means\u2014\n**(A)**\nthe Department of Housing and Urban Development, including the Federal Housing Administration and the Government National Mortgage Association;\n**(B)**\nthe Department of Veterans Affairs;\n**(C)**\nthe Department of Agriculture;\n**(D)**\nthe Federal National Mortgage Association;\n**(E)**\nthe Federal National Mortgage Corporation; and\n**(F)**\nany other Federal agency that is selling or otherwise disposing of covered residential property.\n**(2) Covered residential property**\nThe term covered residential property \u2014\n**(A)**\nmeans residential real property or a manufactured housing community; and\n**(B)**\ndoes not include\u2014\n**(i)**\nFederally assisted housing, as defined in section 579 of the Quality Housing and Work Responsibility Act of 1998 ( 42 U.S.C. 13664 ); or\n**(ii)**\nany residential property that uses tax credits under section 42 of the Internal Revenue Code of 1986.\n**(3) Federally backed mortgage loan**\nThe term Federally backed mortgage loan has the meaning given the term in section 4022(a) of the CARES Act ( 15 U.S.C. 9056(a) ).\n**(4) Institutional investment entity; large owner**\nThe terms institutional investment entity and large owner have the meanings given those terms in subparagraphs (A) and (B)(i) of section 163(n)(7) of the Internal Revenue Code of 1986, as added by this Act.\n**(5) Manufactured housing community**\nThe term manufactured housing community means a residential real estate development with lots on which factory-built homes, including manufactured homes (as defined in section 603 of the National Manufactured Housing Construction and Safety Standards Act of 1974 ( 42 U.S.C. 5402 )), are located, together with supporting infrastructure.\n**(6) Residential real property**\nThe term residential real property has the meaning given the term in section 1004 of the Residential Lead-Based Paint Hazard Reduction Act of 1992 ( 42 U.S.C. 4851b ).\n##### (b) Prohibition on sale\nA covered entity may not sell or otherwise dispose of Federally backed mortgage loans or covered residential properties to a large owner or an institutional investment entity, including a loan or property that is\u2014\n**(1)**\na nonperforming or re-performing loan;\n**(2)**\na foreclosed home;\n**(3)**\na real estate-owned property; or\n**(4)**\nany other real estate-related asset held by the covered entity.\n##### (c) Prohibition on financing\n**(1) In general**\nA covered entity may not issue, insure, guarantee, or securitize any mortgage loan where the borrower is a large owner or an institutional investment entity, unless the mortgage loan is related to\u2014\n**(A)**\nthe construction or rehabilitation of housing with affordability use restrictions; or\n**(B)**\nthe refinance of existing loans related to such housing, and such refinance will not result in the elimination of affordability use restrictions.\n**(2) Application**\nThe prohibition under paragraph (1) shall not apply with respect to a mortgage loan that is issued, insured, guaranteed, or securitized before the date of enactment of this Act.\n#### 5. Investments in housing supply and homeownership\n##### (a) Definitions\nIn this section:\n**(1) Heir property**\nThe term heir property means residential property for which title passed by operation of law through intestacy and is held by 2 or more heirs as tenants in common.\n**(2) Qualified homebuyer**\nThe term qualified homebuyer means a homebuyer that meets all of the following requirements:\n**(A) Income**\nThe household of the homebuyer has an income that does not exceed\u2014\n**(i)**\n120 percent of median income for the area (as determined by the Secretary of Housing and Urban Development) within which\u2014\n**(I)**\nthe home to be acquired using assistance under this section is located; or\n**(II)**\nthe place of residence of the homebuyer is located; or\n**(ii)**\nin the case of a homebuyer acquiring a home that is located in a high-cost area, as determined by the Secretary of Housing and Urban Development, 140 percent of the median income for the area within which the home to be acquired using assistance under this section is located.\n**(B) First-time homebuyer**\nThe homebuyer, as self-attested by the homebuyer, is a first-time homebuyer, as defined in section 104 of the Cranston Gonzalez National Affordable Housing Act ( 42 U.S.C. 12704 ), except that\u2014\n**(i)**\nfor the purposes of this section, the reference in such section 104 to title II shall be considered to refer to this section; and\n**(ii)**\nownership of heir property shall not be treated as owning a home for purposes of determining whether a borrower qualifies as a first-time homebuyer.\n**(C) First-generation homebuyer**\nThe homebuyer, as self-attested by the homebuyer, is\u2014\n**(i)**\nan individual\u2014\n**(I)**\nwhose parents or legal guardians do not, or did not at the time of their death, to the best of the individual\u2019s knowledge, have any present ownership interest in a residence in any State, excluding ownership of heir property or ownership of chattel; and\n**(II)**\nwhose spouse or domestic partner has not, during the 3-year period ending upon acquisition of the eligible home to be acquired using such assistance, had any present ownership interest in a residence in any State, excluding ownership of heir property or ownership of chattel, whether the individual is a co-borrower on the loan or not; or\n**(ii)**\nan individual who has at any time been placed in foster care or institutional care whose spouse or domestic partner has not, during the 3-year period ending upon acquisition of the home to be acquired using assistance under this section, had any ownership interest in a residence in any State, excluding ownership of heir property or ownership of chattel, whether such individuals are co-borrowers on the loan or not.\n##### (b) Transfers\nFor fiscal year 2026 and each fiscal year thereafter, there are hereby appropriated amounts equal to the following percentages of savings (as estimated by the Secretary of the Treasury) resulting from the limits on deductions established under sections 163(n) and 167(i) of the Internal Revenue Code of 1986, as added by this Act:\n**(1)**\n80 percent of such amounts to the Secretary of Housing and Urban Development to provide additional funding for the HOME Investment Partnerships program under subtitle A of title II of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 12741 et seq. ), to be allocated in accordance with the formula under that program, except that such amounts shall not be subject to the requirements under section 231 of such Act ( 42 U.S.C. 12771 ), for the following purposes:\n**(A)**\nAcquisition of affordable housing, and associated rehabilitation or preservation of such acquired housing.\n**(B)**\n60 percent of the 80 percent under this paragraph to be used for new construction of affordable housing, with at least half of such funds to be used for new construction of affordable housing for the benefit of extremely low-income households.\n**(2)**\n20 percent of such amounts to the Secretary of Housing and Urban Development to establish a fund to provide grants of assistance on behalf of qualified homebuyers, the amount of which shall not exceed the greater of $20,000 or 10 percent of the purchase price for each qualified homebuyer, for down payments, closing costs, and interest rate buydowns associated with acquiring owner-occupied primary residences.\n#### 6. Increase antitrust monitoring for real property owners\n##### (a) Housing acquisitions review and transparency\n**(1) Definitions**\nIn this section:\n**(A) Residential property**\nThe term residential property \u2014\n**(i)**\nmeans property that is zoned or intended to be used as a dwelling for individuals or households, including multifamily housing, condominiums, manufactured homes, or single-family homes; and\n**(ii)**\ndoes not include any place of short-term lodging.\n**(B) Investment rental property**\nThe term investment rental property means real property that\u2014\n**(i)**\nwill not be rented to an entity, including any entity of the acquiring person, except for the sole purpose of maintaining, managing, or supervising the operation of the real property; and\n**(ii)**\nwill be held solely for rental or investment purposes.\n**(C) Place of short-term lodging**\nThe term place of short-term lodging means a hotel, motel, inn, short-term rental, or other place of lodging that advertises at a price that is a nightly, hourly, or weekly rate.\n**(2) Amendments making housing transactions reportable**\n**(A) Single acquisition**\nSection 7A(a) of the Clayton Act ( 15 U.S.C. 18a(a) ) is amended by adding at the end the following: For purposes of this subsection, all acquisitions of residential property (as defined in section 6(a) of the American Homeownership Act by any person within a single calendar year shall be deemed to be a single acquisition and notification pursuant to this subsection shall be filed by the acquiring person upon acquiring the property that brings such single acquisition within any requirement described in paragraph (2) when aggregated with all other prior acquisitions of residential property by the person in that calendar year. .\n**(B) Exemption**\nSection 7A(c)(1) of the Clayton Act ( 15 U.S.C. 18a(c)(1) ) is amended by inserting , unless the transaction includes residential property or investment rental property (as defined in section 6(a) of the American Homeownership Act ), including in the form of a real estate investment trust, that is not solely intended for the personal use of an individual. .\n**(C) Code of Federal Regulations**\nThe Federal Trade Commission, with the concurrence of the Assistant Attorney General in charge of the Antitrust Division of the Department of Justice, shall, by rule, in accordance with section 553 of title 5, United States Code\u2014\n**(i)**\namend part 802 of title 16, Code of Federal Regulations to conform with the amendments to section 7A(a) of the Clayton Act ( 15 U.S.C. 18(a) ) made by this paragraph; and\n**(ii)**\nrescind any rules exempting residential property or investment rental property pursuant to section 7A(d)(2)(B) of that Act.\n**(3) Rulemaking**\nThe Federal Trade Commission, with the concurrence of the Assistant Attorney General in charge of the Antitrust Division of the Department of Justice and by rule, in accordance with section 553 of title 5, United States Code, shall issue rules relating to the form and documentary material and information relevant to any acquisition or aggregated acquisitions of residential property is necessary and appropriate under section 7A(a) of the Clayton Act ( 15 U.S.C. 18a(a) ), as amended by paragraph (2), to enable the Federal Trade Commission and the Assistant Attorney General to determine whether such acquisition or aggregated acquisitions may violate the antitrust laws, as defined in subsection (a) of the first section of the Clayton Act ( 15 U.S.C. 12 ).\n##### (b) Presumption of unlawful merger or acquisition\n**(1) Sense of Congress**\nIt is the sense of Congress that\u2014\n**(A)**\nmarket concentration and the change in market concentration due to a merger or acquisition can be an important indicator of the merger or acquisition\u2019s risk of substantially lessening competition; and\n**(B)**\nin a landmark case, the Supreme Court correctly explained that the intense congressional concern with the trend toward concentration warrants dispensing, in certain cases, with elaborate proof of market structure, market behavior, or probable anticompetitive effects. United States v. Philadelphia National Bank, 374 U.S. 321 (1963).\n**(2) Presumption**\n**(A) In general**\nFor the avoidance of doubt, the Department of Justice and the Federal Trade Commission shall apply the presumption that an acquisition involving residential property increasing the relevant market share of the acquiring person to more than 30 percent violates the antitrust laws, as defined in subsection (a) of the first section of the Clayton Act ( 15 U.S.C. 12 ), and that such acquisition constitutes an unfair method of competition under section 5 of the Federal Trade Commission Act ( 15 U.S.C. 45 ).\n**(B) Rule of construction**\nThe clarification described in subparagraph (A) shall not be read to limit the use of the presumption under that subparagraph in other markets, cast doubt on other presumptions in antitrust enforcement, or suggest that a market share that is less than 30 percent is presumptively lawful.",
      "versionDate": "2026-02-24",
      "versionType": "Introduced in Senate"
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
        "name": "Taxation",
        "updateDate": "2026-03-13T22:31:13Z"
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
      "date": "2026-02-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3904is.xml"
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
      "title": "American Homeownership Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-12T04:23:29Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "American Homeownership Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-12T04:23:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to deny interest and depreciation deductions for certain taxpayers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-12T04:18:30Z"
    }
  ]
}
```
