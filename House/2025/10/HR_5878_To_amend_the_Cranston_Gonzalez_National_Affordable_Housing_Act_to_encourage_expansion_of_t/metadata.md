# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5878?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5878
- Title: HOME Reform Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5878
- Origin chamber: House
- Introduced date: 2025-10-31
- Update date: 2026-01-31T03:11:14Z
- Update date including text: 2026-01-31T03:11:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-10-31: Introduced in House
- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-10-31: Introduced in House

## Actions

- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-31",
    "latestAction": {
      "actionDate": "2025-10-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5878",
    "number": "5878",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "F000474",
        "district": "1",
        "firstName": "Mike",
        "fullName": "Rep. Flood, Mike [R-NE-1]",
        "lastName": "Flood",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "HOME Reform Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-31T03:11:14Z",
    "updateDateIncludingText": "2026-01-31T03:11:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-31",
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
      "actionDate": "2025-10-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-31",
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
          "date": "2025-10-31T17:01:30Z",
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
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5878ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5878\nIN THE HOUSE OF REPRESENTATIVES\nOctober 31, 2025 Mr. Flood (for himself and Mr. Cleaver ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the Cranston-Gonzalez National Affordable Housing Act to encourage expansion of the supply of decent, safe, sanitary, and affordable housing, with primary attention to rental housing, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the HOME Reform Act of 2025 .\n#### 2. Definitions; assistance for low-income families\n##### (a) Definitions\nSection 104 of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 12704 ) is amended\u2014\n**(1)**\nin paragraph (6)(B), by striking significant ; and\n**(2)**\nby adding at end the following new paragraph:\n(26) The term infill housing project means a residential housing project that\u2014 (A) is located within the geographic limits of a municipality; (B) is adequately served by existing utilities and public services as required under applicable law; (C) is located on a site of previously disturbed land of not more than 5 acres; and (D) is substantially surrounded by residential or commercial development, as determined by the Secretary. .\n##### (b) Assistance for low-Income families\nTitle II of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 12721 et seq. ) is amended\u2014\n**(1)**\nin section 214(2), by striking households that qualify as low-income families and inserting families with a household income that does not exceed 100 percent of the median family income of the area, as determined by the Secretary with adjustments for smaller and larger families ;\n**(2)**\nin section 215\u2014\n**(A)**\nin subsection (b)(2), by striking whose family qualifies as a low-income family and inserting with a family income that does not exceed 100 percent of the median family income of the area as determined by the Secretary with adjustments for smaller and larger families ; and\n**(B)**\nin subsection (b)(3)(A)(ii), by striking low-income homebuyers and inserting homebuyers with a household income that does not exceed 100 percent of the median family income of the area, as determined by the Secretary with adjustments for smaller and larger families ; and\n**(3)**\nin section 271(c)\u2014\n**(A)**\nin paragraph (1)(B), by striking low-income and inserting families with a household income that does not exceed 100 percent of the median family income of the area as determined by the Secretary with adjustments for smaller and larger families ; and\n**(B)**\nin paragraph (2)(A), by striking low-income families and inserting families with a household income that does not exceed 100 percent of the median family income of the area as determined by the Secretary with adjustments for smaller and larger families .\n#### 3. Choices made by participating jurisdictions\nSection 212(a)(2) of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 12742 ) is amended to read as follows:\n(2) Limitation on restrictions The Secretary shall not restrict a participating jurisdiction\u2019s choice of rehabilitation, substantial rehabilitation, new construction, reconstruction, acquisition, or other eligible housing use unless such restriction is explicitly authorized under section 223(2). .\n#### 4. Use of amounts by certain jurisdictions for infrastructure improvements\n##### (a) Use of investments for housing uses\n**(1) In general**\nSection 212(a) of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 12742(a) ) is amended by inserting after paragraph (3) the following new paragraph:\n(4) Infrastructure improvements in nonentitlement areas (A) In general In accordance with regulations to be issued by the Secretary, funds provided under this subtitle may be used for infrastructure improvements, including the installation or repair of water and sewer lines, sidewalks, roads, and utility connections, in any jurisdiction that does not receive assistance under title I of the Housing and Community Development Act of 1974, if such improvements are directly related to, and located within or immediately adjacent to\u2014 (i) housing assisted under this subtitle; or (ii) housing assisted by section 42 of the Internal Revenue Code of 1986. (B) Application of labor standards The labor standards and requirements set forth in section 110 of the Housing and Community Development Act of 1974 ( 42 U.S.C. 5310 ) shall apply to any infrastructure improvements assisted with funds provided under this subtitle. .\n**(2) Issuance of rules**\nNot later than 1 year after the date of the enactment of this Act, the Secretary shall issue such rules as the Secretary determines necessary to carry out the amendment made by paragraph (1).\n**(3) Rule of construction**\nNothing in the amendment made by paragraph (1) shall be construed to impose any requirements of the HOME Investment Partnerships program on housing that benefits from the infrastructure improvements described in such amendment but otherwise does not receive any assistance from such program.\n##### (b) Per unit investment limitations\nSection 212(e)(1) of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 12742(e)(1) ) is amended by striking the second sentence.\n#### 5. Affordable rental housing qualifications\nSection 215(a) of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 12745(a) ) is amended by adding at the end the following new paragraph:\n(7) Exception for housing choice vouchers Notwithstanding paragraph (1)(A), a rental unit shall be considered to qualify as affordable housing under this title if\u2014 (A) the unit is occupied by a tenant receiving tenant-based rental assistance under section 8 of the United States Housing Act of 1937 ( 42 U.S.C. 1437f ); (B) the tenant\u2019s contribution toward rent does not exceed the amount permitted under such section 8 assistance; and (C) the total rent for the unit does not exceed the amount approved by the public housing agency administering the assistance under that program. .\n#### 6. Affordable homeownership housing qualifications\nSection 215 of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 12745(b) ) is amended\u2014\n**(1)**\nin subsection (b),\n**(A)**\nin paragraph (1), by striking 95 percent and inserting 110 percent ;\n**(B)**\nin paragraph (3)\u2014\n**(i)**\nin subparagraph (A)(ii), by striking or at the end;\n**(ii)**\nin subparagraph (B), by striking and at the end and inserting or ; and\n**(iii)**\nby adding at the end the following new subparagraph:\n(C) maintain long-term affordability through a shared equity ownership model, a community land trust, a limited equity cooperative, a community development corporation, or other mechanism approved by the Secretary, that preserves affordability for future eligible homebuyers and ensures compliance with the purposes of this title, including through the use of purchase options, rights of first refusal or other preemptive rights to purchase housing; and ; and\n**(2)**\nby adding at the end the following:\n(c) Permissible exceptions related to homeownership qualifications (1) Military members A participating jurisdiction, in accordance with terms established by the Secretary, may suspend or waive the income qualifications described in subsection (b)(2) with respect to housing that otherwise meets the criteria under subsection (b) if the owner of the housing\u2014 (A) is a member of a regular component of the armed forces or a member of the National Guard on full-time National Guard duty, active Guard and Reserve duty, or inactive-duty training (as those terms are defined in section 101(d) of title 10, United States Code); and (B) has received\u2014 (i) temporary duty orders to deploy with a military unit or military orders to deploy as an individual acting in support of a military operation, to a location that is not within a reasonable distance from the housing, as determined by the Secretary, for a period of not less than 90 days; or (ii) orders for a permanent change of station. (2) Suspension or waiver of requirements for heir or beneficiary of deceased owner Notwithstanding subsection (b)(3), housing that meets the criteria under that subsection prior to the death of an owner may continue to qualify as affordable housing if\u2014 (A) the housing is the principal residence of an heir or beneficiary of the deceased owner, as defined by the Secretary; and (B) the heir or beneficiary, in accordance with terms established by the Secretary, assumes the duties and obligations of the deceased owner with respect to funds provided under this title. .\n#### 7. Removal of expiration of right to draw home investment trust funds\nSection 218 of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 12748 ) is amended\u2014\n**(1)**\nby striking subsection (g); and\n**(2)**\nby redesignating subsection (h) as subsection (g).\n#### 8. Adjusted recapture and reuse of set-aside for community housing developmental organizations\nSection 231(b) of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 12771(b) ) is amended to read as follows:\n(b) Recapture and reuse If any funds reserved under subsection (a) remain uninvested for a period of 24 months, the Secretary shall make such funds available to the participating jurisdiction for any eligible activities under title II of this Act without regard to whether a community housing development organization materially participates in the use of funds. .\n#### 9. Asset recycling information dissemination expansion\nSection 245(b)(2) of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 12785(b)(2) ) is amended by striking 95 percent and inserting 110 percent .\n#### 10. Environmental review requirements\n##### (a) Categorical exemptions; removing duplicative reviews\nSection 288 of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 12838 ) is amended by adding at the end the following new subsections:\n(e) Categorical exemptions The following categories of activities carried out under this title shall be statutorily exempt from environmental review under the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ), and shall not require further review under such Act\u2014 (1) new construction infill housing projects; (2) acquisition of real property for affordable housing purposes; (3) rehabilitation projects carried out pursuant to section 212(a)(1); and (4) new construction projects of 15 units or less. (f) Removing duplicative reviews (1) In general To the extent practicable and permitted by law, the Secretary shall ensure that a project that has undergone an environmental review under this section shall not be subject to a duplicative environmental review solely due to the addition, substitution, or reallocation of other sources of Federal assistance, if the scope, scale, and location of the project remain substantially unchanged. (2) Coordination of environmental review responsibilities The Secretary shall, by regulation, provide for coordination of environmental review responsibilities with other Federal agencies to streamline inter-agency compliance and avoid unnecessary duplication of effort under the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ) and other applicable laws. (3) Recognition of prior reviews by responsible entities A project may not be subject to an environmental review under this section if a substantially similar review has already been completed by an entity designated under section 104(g)(1) of the Housing and Community Development Act of 1974 ( 42 U.S.C. 5304(g)(1) ) or by another entity the Secretary determines to have equivalent authority, if the scope, scale, and location of the project remain substantially unchanged. .\n##### (b) Issuance of rules\nNot later than 1 year after the date of the enactment of this Act, the Secretary shall issue such rules as the Secretary determines necessary to carry out the amendment made by this subsection.\n#### 11. Application of other specified statutory requirements\nTitle II of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 12721 et seq. ) is amended by adding at the end the following new sections:\n291. Application of build America, buy America requirements With respect to activities assisted under this title, requirements under the Build America, Buy America Act ( 41 U.S.C. 8301 note) and any implementing regulations or guidance, shall only apply to infrastructure improvements conducted under section 212(a)(4) using funds provided under subtitle A. 292. Nonapplicability of certain requirements for small projects Notwithstanding any other provision of law, the requirements of section 3 of the Housing and Urban Development Act of 1968 ( 12 U.S.C. 1701u ), and any implementing regulations or guidance, shall not apply to any activity assisted under title that involves rehabilitation, construction, or other development of housing if the total number of dwelling units assisted under the activity is 50 or fewer and if such assistance is provided to\u2014 (1) a State recipient pursuant to section 216; or (2) a participating jurisdiction that received a total allocation of less than $3,000,000 in the most recent fiscal year pursuant to section 216. .\n#### 12. Technical amendments\nThe Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 12701 et seq. ) is amended\u2014\n**(1)**\nby striking Stewart B. McKinney Homeless Assistance Act each place it appears and inserting McKinney-Vento Homeless Assistance Act ; and\n**(2)**\nby striking Committee on Banking, Finance and Urban Affairs each place it appears and inserting Committee on Financial Services .",
      "versionDate": "2025-10-31",
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
        "actionDate": "2025-10-21",
        "text": "Referred to the House Committee on Financial Services."
      },
      "number": "5798",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "HOME Reform Act of 2025",
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
        "name": "Housing and Community Development",
        "updateDate": "2025-11-25T19:00:03Z"
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
      "date": "2025-10-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5878ih.xml"
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
      "title": "HOME Reform Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-04T10:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HOME Reform Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-04T10:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Cranston-Gonzalez National Affordable Housing Act to encourage expansion of the supply of decent, safe, sanitary, and affordable housing, with primary attention to rental housing, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-04T10:48:18Z"
    }
  ]
}
```
