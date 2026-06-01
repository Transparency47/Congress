# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1177?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1177
- Title: Improve and Enhance the Work Opportunity Tax Credit Act
- Congress: 119
- Bill type: HR
- Bill number: 1177
- Origin chamber: House
- Introduced date: 2025-02-10
- Update date: 2025-12-05T22:02:10Z
- Update date including text: 2025-12-05T22:02:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-10: Introduced in House
- 2025-02-10 - IntroReferral: Introduced in House
- 2025-02-10 - IntroReferral: Introduced in House
- 2025-02-10 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-02-10: Introduced in House

## Actions

- 2025-02-10 - IntroReferral: Introduced in House
- 2025-02-10 - IntroReferral: Introduced in House
- 2025-02-10 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-10",
    "latestAction": {
      "actionDate": "2025-02-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1177",
    "number": "1177",
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
    "updateDate": "2025-12-05T22:02:10Z",
    "updateDateIncludingText": "2025-12-05T22:02:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-10",
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
      "actionDate": "2025-02-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-10",
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
          "date": "2025-02-10T17:02:25Z",
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
      "sponsorshipDate": "2025-02-10",
      "state": "NV"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "PA"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-02-10",
      "state": "NY"
    },
    {
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "PA"
    },
    {
      "bioguideId": "B001260",
      "district": "16",
      "firstName": "Vern",
      "fullName": "Rep. Buchanan, Vern [R-FL-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Buchanan",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "FL"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "GA"
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
      "sponsorshipDate": "2025-02-14",
      "state": "WV"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "NY"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "CA"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "NY"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "DE"
    },
    {
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "OH"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
      "state": "NJ"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "CO"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-09-19",
      "state": "KS"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1177ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1177\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 10, 2025 Mr. Smucker (for himself, Mr. Horsford , Mr. Fitzpatrick , Mr. Suozzi , Mr. Kelly of Pennsylvania , and Mr. Buchanan ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to improve and enhance the work opportunity tax credit, to encourage longer-service employment, and to modernize the credit to make it more effective as a hiring incentive for targeted workers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Improve and Enhance the Work Opportunity Tax Credit Act .\n#### 2. Improving and enhancing work opportunity tax credit\n##### (a) In general\nSection 51(a) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking shall be equal to 40 percent and all that follows and inserting the following:\nshall be equal to the sum of\u2014 (1) 50 percent of so much of the qualified first-year wages with respect to each individual for such year as does not exceed $6,000, plus (2) in the case of individuals who have performed at least 400 hours of service for the employer, 50 percent of so much of the qualified first-year wages with respect to each such individual for such year as exceeds $6,000, and does not exceed $12,000. .\n##### (b) Conforming amendments relating to limitation on wages taken into account for certain veterans\nSection 51(b)(3) of such Code is amended to read as follows:\n(3) Increased limitation on wages taken into account for veterans The $6,000 and $12,000 amounts under paragraphs (1) and (2) of subsection (a) shall be increased to\u2014 (A) $12,000 and $24,000, respectively, in the case of any individual who is a qualified veteran by reason of subsection (d)(3)(A)(ii)(I), (B) $14,000 and $28,000, respectively, in the case of any individual who is a qualified veteran by reason of subsection (d)(3)(A)(iv), and (C) $24,000 and $48,000, respectively, in the case of any individual who is a qualified veteran by reason of subsection (d)(3)(A)(ii)(II). .\n##### (c) Conforming amendments relating to individuals not meeting minimum employment periods\n**(1)**\nSubparagraphs (A) and (B) of section 51(i)(3) of such Code are each amended by striking subsection (a) and inserting subsection (a)(1) .\n**(2)**\nSection 51(i)(3)(A) of such Code is amended by striking 40 percent and inserting 50 percent .\n##### (d) Conforming amendments relating to treatment of summer youth employees\nSection 51(d)(7)(B) of such Code is amended\u2014\n**(1)**\nby striking clause (ii),\n**(2)**\nby striking , and at the end of clause (i) and inserting a period,\n**(3)**\nby redesignating clause (i) (as so amended) as clause (iv), and\n**(4)**\nby inserting before such clause (iv) (as so redesignated) the following new clauses:\n(i) in lieu of the amount determined under subsection (a), the amount of the work opportunity credit determined under this section for the taxable year shall be equal to 40 percent of the qualified first-year wages for such year, (ii) in the case of an individual described in subsection (i)(3)(A), clause (i) shall be applied by substituting 25 percent for 40 percent , (iii) in the case of an individual described in subsection (i)(3)(B), no wages shall be taken into account under clause (i), (iv) the amount of qualified first-year wages which may be taken into account with respect to such individual shall not exceed $3,000 per year, and .\n##### (e) Conforming amendments relating to long-Term family assistance recipients\n**(1) In general**\nSection 51(e)(1) of such Code is amended by striking family assistance recipient\u2014 and all that follows and inserting the following:\nfamily assistance recipient, in lieu of subsection (a), the amount of the work opportunity credit determined under this section for the taxable year shall be equal to\u2014 (1) 40 percent of so much of the qualified first-year wages with respect to such individual for such year as does not exceed $10,000, and (2) 50 percent of so much of the qualified second-year wages with respect to such individual for such year as does not exceed $10,000. .\n**(2) Clerical amendment**\nThe heading for section 51(e) of such Code is amended by striking Credit for second-year wages and inserting Special rules for determining credit .\n##### (f) Effective date\nThe amendments made by this section shall apply to individuals who begin work for the employer after December 31, 2024.\n#### 3. Removal of age limit for qualified supplemental nutrition assistance program benefits recipient\n##### (a) In general\nSection 51(d)(8)(A)(i) of the Internal Revenue Code of 1986 is amended by striking but not age 40 .\n##### (b) Effective date\nThe amendment made by this section shall apply to individuals who begin work for the employer after December 31, 2024.",
      "versionDate": "2025-02-10",
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
        "actionDate": "2025-02-10",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "492",
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
        "updateDate": "2025-05-06T12:44:53Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-10",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr1177",
          "measure-number": "1177",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-10",
          "originChamber": "HOUSE",
          "update-date": "2025-09-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1177v00",
            "update-date": "2025-09-23"
          },
          "action-date": "2025-02-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Improve and Enhance the Work Opportunity Tax Credit Act </strong></p><p>This bill increases the work opportunity tax credit (WOTC) for wages paid during the first year of employment to certain employees. The bill also eliminates the maximum age limit applicable to Supplemental Nutrition Assistance Program (SNAP) benefit recipients for purposes of the WOTC.</p><p>Under current law, an employer generally may claim a WOTC in the amount of 40% of up to $6,000 (or of up to $24,000 for certain veterans, $3,000 for summer youth employees, and $10,000 for long-term family aid recipients) of qualified wages paid during the first year of employment to an employee who is a member of a targeted group. (Exceptions and limitations apply.)</p><p>The bill increases the WOTC to (1) 50% of up to $6,000 (or of up to $24,000 for certain veterans) of qualified first-year wages paid to an employee who is a member of a targeted group (other than a summer youth employee or recipient of long-term family aid), and (2) 50% of up to $12,000 (or of up to $48,000 for certain veterans) of qualified wages paid during the first year of employment to such employee if the employee works at least 400 hours during the year.</p><p>Finally, the bill eliminates the maximum age limit applicable to SNAP benefit recipients and, thus, allows an employer to claim the\u00a0WOTC for qualified first-year wages paid to an employee who is at least 18 years old and\u00a0receiving SNAP benefits for a certain period of time.</p>"
        },
        "title": "Improve and Enhance the Work Opportunity Tax Credit Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1177.xml",
    "summary": {
      "actionDate": "2025-02-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Improve and Enhance the Work Opportunity Tax Credit Act </strong></p><p>This bill increases the work opportunity tax credit (WOTC) for wages paid during the first year of employment to certain employees. The bill also eliminates the maximum age limit applicable to Supplemental Nutrition Assistance Program (SNAP) benefit recipients for purposes of the WOTC.</p><p>Under current law, an employer generally may claim a WOTC in the amount of 40% of up to $6,000 (or of up to $24,000 for certain veterans, $3,000 for summer youth employees, and $10,000 for long-term family aid recipients) of qualified wages paid during the first year of employment to an employee who is a member of a targeted group. (Exceptions and limitations apply.)</p><p>The bill increases the WOTC to (1) 50% of up to $6,000 (or of up to $24,000 for certain veterans) of qualified first-year wages paid to an employee who is a member of a targeted group (other than a summer youth employee or recipient of long-term family aid), and (2) 50% of up to $12,000 (or of up to $48,000 for certain veterans) of qualified wages paid during the first year of employment to such employee if the employee works at least 400 hours during the year.</p><p>Finally, the bill eliminates the maximum age limit applicable to SNAP benefit recipients and, thus, allows an employer to claim the\u00a0WOTC for qualified first-year wages paid to an employee who is at least 18 years old and\u00a0receiving SNAP benefits for a certain period of time.</p>",
      "updateDate": "2025-09-23",
      "versionCode": "id119hr1177"
    },
    "title": "Improve and Enhance the Work Opportunity Tax Credit Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Improve and Enhance the Work Opportunity Tax Credit Act </strong></p><p>This bill increases the work opportunity tax credit (WOTC) for wages paid during the first year of employment to certain employees. The bill also eliminates the maximum age limit applicable to Supplemental Nutrition Assistance Program (SNAP) benefit recipients for purposes of the WOTC.</p><p>Under current law, an employer generally may claim a WOTC in the amount of 40% of up to $6,000 (or of up to $24,000 for certain veterans, $3,000 for summer youth employees, and $10,000 for long-term family aid recipients) of qualified wages paid during the first year of employment to an employee who is a member of a targeted group. (Exceptions and limitations apply.)</p><p>The bill increases the WOTC to (1) 50% of up to $6,000 (or of up to $24,000 for certain veterans) of qualified first-year wages paid to an employee who is a member of a targeted group (other than a summer youth employee or recipient of long-term family aid), and (2) 50% of up to $12,000 (or of up to $48,000 for certain veterans) of qualified wages paid during the first year of employment to such employee if the employee works at least 400 hours during the year.</p><p>Finally, the bill eliminates the maximum age limit applicable to SNAP benefit recipients and, thus, allows an employer to claim the\u00a0WOTC for qualified first-year wages paid to an employee who is at least 18 years old and\u00a0receiving SNAP benefits for a certain period of time.</p>",
      "updateDate": "2025-09-23",
      "versionCode": "id119hr1177"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1177ih.xml"
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
      "title": "Improve and Enhance the Work Opportunity Tax Credit Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T06:38:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Improve and Enhance the Work Opportunity Tax Credit Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T06:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to improve and enhance the work opportunity tax credit, to encourage longer-service employment, and to modernize the credit to make it more effective as a hiring incentive for targeted workers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T06:33:43Z"
    }
  ]
}
```
