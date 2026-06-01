# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7460?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7460
- Title: Airborne Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7460
- Origin chamber: House
- Introduced date: 2026-02-10
- Update date: 2026-05-05T08:05:45Z
- Update date including text: 2026-05-05T08:05:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-10: Introduced in House
- 2026-02-10 - IntroReferral: Introduced in House
- 2026-02-10 - IntroReferral: Introduced in House
- 2026-02-10 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-02-10: Introduced in House

## Actions

- 2026-02-10 - IntroReferral: Introduced in House
- 2026-02-10 - IntroReferral: Introduced in House
- 2026-02-10 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-10",
    "latestAction": {
      "actionDate": "2026-02-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7460",
    "number": "7460",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "B001292",
        "district": "8",
        "firstName": "Donald",
        "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
        "lastName": "Beyer",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Airborne Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-05T08:05:45Z",
    "updateDateIncludingText": "2026-05-05T08:05:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-10",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-10",
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
          "date": "2026-02-10T15:02:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "PA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "DC"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "NY"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "False",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "CA"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "CO"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2026-05-04",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7460ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7460\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 10, 2026 Mr. Beyer (for himself and Mr. Fitzpatrick ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide a tax credit for certain indoor air quality assessments and improvements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Airborne Act of 2026 .\n#### 2. Indoor air quality credit\n##### (a) In general\nSubpart D of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n45BB. Indoor air quality credit (a) Allowance of credit (1) In general For purposes of section 38, the indoor air quality credit determined under this section for the taxable year is an amount equal to the sum of\u2014 (A) the applicable amount with respect to a qualified indoor air quality assessment of a qualifying property during such taxable year, plus (B) the applicable amount with respect to any qualified air cleaning system upgrade or qualified HVAC upgrade placed in service at such qualifying property during such taxable year. (2) Applicable amount (A) In general For purposes of paragraph (1), the applicable amount is\u2014 (i) in the case of a qualified indoor air quality assessment, $1 per square foot of property affected by such assessment, (ii) in the case of a qualified air cleaning system upgrade, $5 per square foot of property affected by such upgrade, and (iii) in the case of a qualified HVAC upgrade, $50 per square foot of property affected by such upgrade. (B) Increased credit for certain upgrades (i) In general In the case of a qualified air cleaning system upgrade or qualified HVAC upgrade installation that meets the prevailing wage requirements of clause (ii) and the apprenticeship requirements of clause (iii), subparagraph (A) shall be applied\u2014 (I) in clause (ii), by substituting $25 for $5 , and (II) in clause (iii), by substituting $250 for $50 . (ii) Prevailing wage and apprenticeship requirements Rules similar to the rules of section 179D(b)(4) shall apply. (iii) Apprenticeship requirements (I) In general Taxpayers shall ensure that, with respect to the installation of any qualified air cleaning system upgrade or qualified HVAC upgrade, not less than 15 percent of the total labor hours (as defined in section 45(b)(8)(E)(i)) of the construction, alteration, or repair work (including such work performed by any contractor or subcontractor) with respect to such upgrade shall, subject to subclause (II), be performed by qualified apprentices (as defined in section 45(b)(8)(E)(ii)). (II) Apprentice to journeyworker ratio The requirement under subclause (I) shall be subject to any applicable requirements for apprentice-to-journeyworker ratios of the Department of Labor or the applicable State apprenticeship agency. (III) Participation; exception Rules similar to the rules of subparagraphs (C) and (D) of section 45(b)(8) shall apply. (b) Definitions For purposes of this section\u2014 (1) Air cleaning system The term air cleaning system means an air filter, air cleaner, or other system that reduces the concentration of a contaminant in the air by removal, transformation, decomposition, or, in the case of bioaerosols, inactivation. (2) Qualified indoor air quality assessment The term qualified indoor air quality assessment means an assessment of air quality carried out pursuant to the standards described in subsection (c)(1). (3) Qualified air cleaning system upgrade The term qualified air cleaning system upgrade means a new air cleaning system or an air cleaning system repair which\u2014 (A) is placed in service after the date of the enactment of this section at a commercial or public property with respect to which a qualified indoor air quality assessment is completed, (B) is certified pursuant to subsection (c)(2) to bring the commercial or public property on which it is installed into compliance with the American Society of Heating, Refrigerating and Air-Conditioning Engineers (ASHRAE) Standard 62.1\u20132022 or Standard 241\u20132023, and (C) is designed to minimize ventilation energy use by using the Indoor Air Quality Procedure in Section 6.3 of ANSI/ASHRAE Standard 62.1\u20132022 when it is more energy efficient and no more expensive than the alternative Ventilation Rate Procedure in Section 6.2 of Standard ANSI/ASHRAE 62.1\u20132022. (4) Qualified HVAC upgrade The term qualified HVAC upgrade means a new heating, ventilation, and air conditioning system (HVAC) or HVAC repair which is\u2014 (A) placed in service after the date of the enactment of this section at a commercial or public property with respect to which a qualified indoor air quality assessment is completed, (B) is certified pursuant to subsection (c)(3) to bring the commercial or public property on which it is installed into compliance with the American Society of Heating, Refrigerating and Air-Conditioning Engineers (ASHRAE) Standard 62.1\u20132022 or Standard 241\u20132023, and (C) is designed to minimize ventilation energy use by using the Indoor Air Quality Procedure in Section 6.3 of ANSI/ASHRAE Standard 62.1\u20132022 when it is more energy efficient and no more expensive than the alternative Ventilation Rate Procedure in Section 6.2 of ANSI/ASHRAE Standard 62.1\u20132022. (5) Qualifying property The term qualifying property means commercial property, public property, or property owned by an organization described in section 501(c)(3) and exempt from tax under section 501(a). (c) Indoor air quality assessment and certification standards The Secretary shall, after consultation with the Secretary of Energy or the Administrator of the Environmental Protection Agency, as appropriate, prescribe by regulations standards for\u2014 (1) carrying out qualified indoor air quality assessments, (2) certifying air cleaning system upgrades as qualified air cleaning system upgrades, and (3) certifying HVAC upgrades as qualified HVAC upgrades. (d) Limitations (1) Qualified HVAC and qualified air cleaning system upgrades The credit allowed under this section with respect to any taxpayer for any taxable year shall not exceed 50 percent of the total amount expended by the taxpayer during such taxable year for qualified air cleaning system upgrades or qualified HVAC upgrades. (2) Indoor air quality assessments The credit allowed under this section with respect to any taxpayer for any taxable year with respect to qualified indoor air quality assessments shall not exceed the amounts paid or incurred with respect to such assessments. (e) Regulations for allocation of credit with respect to improvements on public property In the case of qualified indoor air quality assessments, qualified air cleaning system upgrades, or qualified HVAC upgrades conducted on or in property owned by a 501(c)(3) organization or by a Federal, State, or local government or a political subdivision thereof, credits with respect to such assessments and upgrades may be allocated, under such regulations as the Secretary shall prescribe, to the person primarily responsible for designing the property. Such person shall be treated as the taxpayer for purposes of this credit. (f) Reduction in basis For purposes of this subtitle, the basis of any property for which a credit is allowable under subsection (a) shall be reduced by the amount of such credit so allowed. (g) Denial of double benefit No deduction shall be allowed under this chapter for any amount taken into account in determining the credit under this section. .\n##### (b) Credit made part of general business credit\nSubsection (b) of section 38 of such Code is amended by striking plus at the end of paragraph (40), by striking the period at the end of paragraph (41) and inserting , plus , and by adding at the end the following new paragraph:\n(42) the indoor air quality credit determined under section 45BB. .\n##### (c) Clerical amendment\nThe table of sections for subpart D of part IV of subchapter A of chapter 1 is amended by adding at the end the following new item:\nSec. 45BB. Indoor Air Quality Credit. .\n##### (d) Effective date\nThe amendments made by this section shall apply to amounts paid or incurred after December 31, 2026, in taxable years ending after such date.\n#### 3. Indoor air quality certification\nNot later than 365 days after the date of the enactment of this Act, the Secretary of Energy, in consultation with the Administrator of the Environmental Protection Agency, shall establish a voluntary certification program through which property owners may certify that their properties are in compliance with the indoor air quality standards of section 45BB(c) of the Internal Revenue Code of 1986, as added by this Act.",
      "versionDate": "2026-02-10",
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
        "name": "Taxation",
        "updateDate": "2026-02-19T18:45:04Z"
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
      "date": "2026-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7460ih.xml"
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
      "title": "Airborne Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-18T09:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Airborne Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-18T09:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to provide a tax credit for certain indoor air quality assessments and improvements, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-18T09:48:25Z"
    }
  ]
}
```
