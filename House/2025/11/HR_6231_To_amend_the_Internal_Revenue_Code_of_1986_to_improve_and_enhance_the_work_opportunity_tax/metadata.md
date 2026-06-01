# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6231?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6231
- Title: Improve and Enhance the Work Opportunity Tax Credit Act
- Congress: 119
- Bill type: HR
- Bill number: 6231
- Origin chamber: House
- Introduced date: 2025-11-20
- Update date: 2026-05-20T08:08:31Z
- Update date including text: 2026-05-20T08:08:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-11-20: Introduced in House

## Actions

- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6231",
    "number": "6231",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S001199",
        "district": "11",
        "firstName": "Lloyd",
        "fullName": "Rep. Smucker, Lloyd [R-PA-11]",
        "lastName": "Smucker",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Improve and Enhance the Work Opportunity Tax Credit Act",
    "type": "HR",
    "updateDate": "2026-05-20T08:08:31Z",
    "updateDateIncludingText": "2026-05-20T08:08:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-20",
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
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-20",
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
          "date": "2025-11-20T15:02:30Z",
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
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "NV"
    },
    {
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "PA"
    },
    {
      "bioguideId": "B001292",
      "district": "8",
      "firstName": "Donald",
      "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Beyer",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "VA"
    },
    {
      "bioguideId": "K000392",
      "district": "8",
      "firstName": "David",
      "fullName": "Rep. Kustoff, David [R-TN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Kustoff",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "TN"
    },
    {
      "bioguideId": "M001213",
      "district": "1",
      "firstName": "Blake",
      "fullName": "Rep. Moore, Blake D. [R-UT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "UT"
    },
    {
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "OH"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "WA"
    },
    {
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-11-25",
      "state": "FL"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-11-25",
      "state": "NY"
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
      "sponsorshipDate": "2025-12-01",
      "state": "PA"
    },
    {
      "bioguideId": "C001126",
      "district": "15",
      "firstName": "Mike",
      "fullName": "Rep. Carey, Mike [R-OH-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Carey",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
      "state": "OH"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "NJ"
    },
    {
      "bioguideId": "M001206",
      "district": "25",
      "firstName": "Joseph",
      "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Morelle",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "NY"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "NY"
    },
    {
      "bioguideId": "M001210",
      "district": "3",
      "firstName": "Gregory",
      "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Murphy",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "NC"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "CA"
    },
    {
      "bioguideId": "M001239",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. McGuire, John J. [R-VA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "McGuire",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "VA"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2026-03-04",
      "state": "NY"
    },
    {
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "GA"
    },
    {
      "bioguideId": "E000299",
      "district": "16",
      "firstName": "Veronica",
      "fullName": "Rep. Escobar, Veronica [D-TX-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Escobar",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "TX"
    },
    {
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "WV"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "NC"
    },
    {
      "bioguideId": "B000740",
      "district": "5",
      "firstName": "Stephanie",
      "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bice",
      "middleName": "I.",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "OK"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6231ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6231\nIN THE HOUSE OF REPRESENTATIVES\nNovember 20, 2025 Mr. Smucker (for himself, Mr. Horsford , Mr. Kelly of Pennsylvania , Mr. Beyer , Mr. Kustoff , Mr. Moore of Utah , Mr. Miller of Ohio , and Ms. DelBene ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to improve and enhance the work opportunity tax credit, to encourage longer-service employment, and to modernize the credit to make it more effective as a hiring incentive for targeted workers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Improve and Enhance the Work Opportunity Tax Credit Act .\n#### 2. Improving and enhancing work opportunity tax credit\n##### (a) Extension\nSection 51(c)(4) of the Internal Revenue Code of 1986 is amended by striking December 31, 2025 and inserting December 31, 2030 .\n##### (b) Enhancement of credit\n**(1) In general**\nSection 51(a) of the Internal Revenue Code of 1986 is amended by striking shall be equal to 40 percent and all that follows and inserting the following:\nshall be equal to the sum of\u2014 (1) 50 percent of so much of the qualified first-year wages with respect to each individual for such year as does not exceed $6,000, plus (2) in the case of individuals who have performed at least 400 hours of service for the employer, 50 percent of so much of the qualified first-year wages with respect to each such individual for such year as exceeds $6,000, and does not exceed twice such dollar amount. .\n**(2) Inflation adjustment**\nSection 51 of such Code is amended by adding at the end the following new subsection:\n(l) Cost-of-Living adjustment (1) In general In the case of any taxable year beginning after 2025, the $6,000 amount in paragraphs (1) and (2) of subsection (a) and the $10,000 amount in subparagraphs (A) and (B) of subsection (e)(1) shall be increased by an amount equal to\u2014 (A) such dollar amount, multiplied by (B) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year in which the taxable year begins, determined by substituting calendar year 2024 for calendar year 2016 in subparagraph (A)(ii) thereof. (2) Rounding Any increase determined under paragraph (1) shall be rounded to the nearest multiple of $100. .\n**(3) Conforming amendments**\n**(A) Limitation on wages taken into account for certain veterans**\nSection 51(b)(3) of such Code is amended to read as follows:\n(3) Increased limitation on wages taken into account for certain veterans (A) In general In the case of a qualified veteran described in subparagraph (B), subsection (a) shall be applied by substituting the applicable amount for $6,000 each place it appears. (B) Applicable amount For purposes of this paragraph, the applicable amount is\u2014 (i) in the case of any individual who is a qualified veteran by reason of subsection (d)(3)(A)(ii)(I), 200 percent of the dollar amount in effect for the taxable year under subsection (a)(1), (ii) in the case of any individual who is a qualified veteran by reason of subsection (d)(3)(A)(iv), 250 percent of the dollar amount in effect for the taxable year under subsection (a)(1), and (iii) in the case of any individual who is a qualified veteran by reason of subsection (d)(3)(A)(ii)(II), 400 percent of the dollar amount in effect for the taxable year under subsection (a)(1). .\n**(B) Summer youth employees**\nSection 51(d)(7)(B) of such Code is amended\u2014\n**(i)**\nby striking clause (ii),\n**(ii)**\nby striking , and at the end of clause (i) and inserting a period,\n**(iii)**\nby redesignating clause (i) (as so amended) as clause (v), and\n**(iv)**\nby inserting before such clause (v) (as so redesignated) the following new clauses:\n(i) in lieu of the amount determined under subsection (a), the amount of the work opportunity credit determined under this section for the taxable year shall be equal to 40 percent of the qualified first-year wages for such year, (ii) in the case of an individual described in subsection (i)(3)(A), clause (i) shall be applied by substituting 25 percent for 40 percent , (iii) in the case of an individual described in subsection (i)(3)(B), no wages shall be taken into account under clause (i), (iv) the amount of qualified first-year wages which may be taken into account with respect to such individual shall not exceed 50 percent of the dollar amount in effect for the taxable year under subsection (a)(1), and .\n**(C) Long-term family assistance recipients**\n**(i) In general**\nSection 51(e)(1) of such Code is amended by striking family assistance recipient\u2014 and all that follows and inserting the following:\nfamily assistance recipient, in lieu of subsection (a), the amount of the work opportunity credit determined under this section for the taxable year shall be equal to\u2014 (A) 40 percent of so much of the qualified first-year wages with respect to such individual for such year as does not exceed $10,000, and (B) 50 percent of so much of the qualified second-year wages with respect to such individual for such year as does not exceed $10,000. .\n**(ii) Clerical amendment**\nThe heading for section 51(e) of such Code is amended by striking Credit for second-year wages and inserting Special rules for determining credit .\n**(D) Agricultural and railway labor**\n**(i) In general**\nSection 51(h)(1) of such Code is amended\u2014\n**(I)**\nby striking $6,000 in subparagraph (A) and inserting the dollar amount in effect for the taxable year under subsection (a)(1) , and\n**(II)**\nby striking $500 per month in subparagraph (B) and inserting 1/12 of the dollar amount in effect under subsection (a)(1) per month .\n**(ii) Related conforming amendments**\nSection 51(e)(3) of such Code is amended by striking subparagraphs (A) and (B) and inserting the following:\n(A) such subparagraph (A) shall be applied by substituting the dollar amount in effect under subsection (e)(1) for the dollar amount in effect under subsection (a)(1) , and (B) such subparagraph (B) shall be applied by substituting one 1/12 of the dollar amount in effect under subsection (e)(1) for 1/12 of the dollar amount in effect under subsection (a)(1) . .\n**(E) Individuals not meeting minimum employment periods**\n**(i)**\nSubparagraphs (A) and (B) of section 51(i)(3) of such Code are each amended by striking subsection (a) and inserting subsection (a)(1) .\n**(ii)**\nSection 51(i)(3)(A) of such Code is amended by striking 40 percent and inserting 50 percent .\n##### (c) Effective date\nThe amendments made by this section shall apply to individuals who begin work for the employer after December 31, 2025.\n#### 3. Removal of age limit for qualified supplemental nutrition assistance program benefits recipient\n##### (a) In general\nSection 51(d)(8)(A)(i) of the Internal Revenue Code of 1986 is amended by striking but not age 40 .\n##### (b) Effective date\nThe amendment made by this section shall apply to individuals who begin work for the employer after December 31, 2025.\n#### 4. Eligibility of spouses of military personnel for the work opportunity credit\n##### (a) In general\nSection 51(d)(1) of the Internal Revenue Code of 1986 is amended by striking or at the end of subparagraph (I), by striking the period at the end of subparagraph (J) and inserting , or , and by adding at the end the following new subparagraph:\n(K) a qualified military spouse. .\n##### (b) Qualified military spouse\nSubsection (d) of section 51 of such Code is amended by adding at the end the following new paragraph:\n(16) Qualified military spouse The term qualified military spouse means any individual who is certified by the designated local agency as being (as of the hiring date) a spouse of a member of the Armed Forces of the United States. .\n##### (c) Effective date\nThe amendments made by this section shall apply to amounts paid or incurred after the date of the enactment of this Act to individuals who begin work for the employer after such date.\n#### 5. Promotion of targeted group member hiring to certain industries\nThe Secretary of the Treasury, the Secretary of Commerce, the Secretary of Labor, and the Administrator of the Small Business Administration (or their respective delegates), in consultation with each other and consistent with applicable law, shall promote the hiring of members of a targeted group (as defined in section 51(d) of the Internal Revenue Code of 1986) to business leaders across critical industry sectors, including manufacturing, infrastructure, energy, health care, and construction.",
      "versionDate": "2025-11-20",
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
        "actionDate": "2025-03-11",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "2033",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Military Spouse Hiring Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-13",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1027",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Military Spouse Hiring Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-11-20",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "3265",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Improve and Enhance the Work Opportunity Tax Credit Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2025-12-12T14:31:40Z"
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
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6231ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to improve and enhance the work opportunity tax credit, to encourage longer-service employment, and to modernize the credit to make it more effective as a hiring incentive for targeted workers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-12T17:24:37Z"
    },
    {
      "title": "Improve and Enhance the Work Opportunity Tax Credit Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-12T14:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Improve and Enhance the Work Opportunity Tax Credit Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-12T14:23:19Z"
    }
  ]
}
```
