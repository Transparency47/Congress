# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3265?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3265
- Title: Improve and Enhance the Work Opportunity Tax Credit Act
- Congress: 119
- Bill type: S
- Bill number: 3265
- Origin chamber: Senate
- Introduced date: 2025-11-20
- Update date: 2026-05-13T11:03:32Z
- Update date including text: 2026-05-13T11:03:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in Senate
- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-11-20: Introduced in Senate

## Actions

- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on Finance.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3265",
    "number": "3265",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "C001075",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Cassidy, Bill [R-LA]",
        "lastName": "Cassidy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Improve and Enhance the Work Opportunity Tax Credit Act",
    "type": "S",
    "updateDate": "2026-05-13T11:03:32Z",
    "updateDateIncludingText": "2026-05-13T11:03:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-20",
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
      "actionDate": "2025-11-20",
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
        "item": [
          {
            "date": "2025-11-20T19:30:05Z",
            "name": "Referred To"
          },
          {
            "date": "2025-11-20T19:30:05Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "NH"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "AR"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "VA"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "KS"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "VT"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "KS"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "WV"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "NV"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "MI"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "MI"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "MT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3265is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3265\nIN THE SENATE OF THE UNITED STATES\nNovember 20, 2025 Mr. Cassidy (for himself, Ms. Hassan , Mr. Boozman , Mr. Kaine , Mr. Marshall , Mr. Welch , Mr. Moran , Mr. Justice , and Ms. Cortez Masto ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to improve and enhance the work opportunity tax credit, to encourage longer-service employment, and to modernize the credit to make it more effective as a hiring incentive for targeted workers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Improve and Enhance the Work Opportunity Tax Credit Act .\n#### 2. Improving and enhancing work opportunity tax credit\n##### (a) Extension\nSection 51(c)(4) of the Internal Revenue Code of 1986 is amended by striking December 31, 2025 and inserting December 31, 2030 .\n##### (b) Enhancement of credit\n**(1) In general**\nSection 51(a) of the Internal Revenue Code of 1986 is amended\u2014\n**(A)**\nby striking shall be equal to 40 percent and all that follows and inserting the following:\nshall be equal to the sum of\u2014 (1) 50 percent of so much of the qualified first-year wages with respect to each individual for such year as does not exceed $6,000, plus (2) in the case of individuals who have performed at least 400 hours of service for the employer, 50 percent of so much of the qualified first-year wages with respect to each such individual for such year as exceeds the dollar amount in effect under paragraph (1) and does not exceed twice such dollar amount. .\n**(2) Inflation adjustments**\nSection 51 of such Code is amended by adding at the end the following new subsection:\n(l) Inflation adjustment (1) In general In the case of any taxable year beginning after 2025, the $6,000 amount in subsections (a)(1) and each of the $10,000 amount in subsection (e)(1) shall be increased by an amount equal to\u2014 (A) such dollar amount, multiplied by (B) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year in which the taxable year begins, determined by substituting calendar year 2024 for calendar year 2016 in subparagraph (A)(ii) thereof. (2) Rounding Any increase determined under paragraph (1) shall be rounded to the next nearest multiple of $100. .\n**(3) Conforming amendments**\n**(A) Limitation on wages taken into account for certain veterans**\nSection 51(b)(3) of such Code is amended to read as follows:\n(3) Increased limitation on wages taken into account for certain veterans (A) In general In the case of any qualified veteran described in subparagraph (B), subsection (a) shall be applied by substituting the applicable amount for $6,000 . (B) Applicable amount For purposes of this paragraph, the applicable amount is\u2014 (i) in the case of any individual who is a qualified veteran by reason of subsection (d)(3)(A)(ii)(I), 200 percent of the dollar amount in effect under subsection (a)(1), (ii) in the case of any individual who is a qualified veteran by reason of subsection (d)(3)(A)(iv), 250 percent of the dollar amount in effect under subsection (a)(1), and (iii) in the case of any individual who is a qualified veteran by reason of subsection (d)(3)(A)(ii)(II), 400 percent of the dollar amount in effect under subsection (a)(1). .\n**(B) Long-term family assistance recipients**\n**(i) In general**\nSection 51(e)(1) of such Code is amended by striking family assistance recipient\u2014 and all that follows and inserting the following:\nfamily assistance recipient, in lieu of subsection (a), the amount of the work opportunity credit determined under this section for the taxable year shall be equal to\u2014 (1) 40 percent of so much of the qualified first-year wages with respect to such individual for such year as does not exceed $10,000, and (2) 50 percent of so much of the qualified second-year wages with respect to such individual for such year as does not exceed $10,000. .\n**(ii) Clerical amendment**\nThe heading for section 51(e) of such Code is amended by striking Credit for second-year wages and inserting Special rules for determining credit .\n**(C) Summer youth employees**\nSection 51(d)(7)(B) of such Code is amended\u2014\n**(i)**\nby striking clause (ii),\n**(ii)**\nby striking , and at the end of clause (i) and inserting a period,\n**(iii)**\nby redesignating clause (i) (as so amended) as clause (v), and\n**(iv)**\nby inserting before such clause (v) (as so redesignated) the following new clauses:\n(i) in lieu of the amount determined under subsection (a), the amount of the work opportunity credit determined under this section for the taxable year shall be equal to 40 percent of the qualified first-year wages for such year, (ii) in the case of an individual described in subsection (i)(3)(A), clause (i) shall be applied by substituting 25 percent for 40 percent , (iii) in the case of an individual described in subsection (i)(3)(B), no wages shall be taken into account under clause (i), (iv) the amount of qualified first-year wages which may be taken into account with respect to such individual shall not exceed 50 percent of the dollar amount in effect under subsection (a)(1), and .\n**(D) Agricultural and railway labor**\n**(i) In general**\nSection 51(h)(1) of such Code is amended\u2014\n**(I)**\nin subparagraph (A), by striking $6,000 and inserting the dollar amount in effect under subsection (a)(1) , and\n**(II)**\nin subparagraph (B), by striking $500 per month and inserting one-twelfth of the dollar amount in effect under subsection (a)(1) per month .\n**(ii) Related conforming amendments**\nSection 51(e)(3) of such Code is amended by striking subparagraphs (A) and (B) and inserting the following:\n(A) such subparagraph (A) shall be applied by substituting the dollar amount in effect under subsection (e)(1) for the dollar amount in effect under subsection (a)(1) , and (B) such subparagraph (B) shall be applied by substituting one-twelfth of the dollar amount in effect under subsection(e)(1) for one-twelfth of the dollar amount in effect under subsection (a)(1) . .\n**(E) Individuals not meeting minimum employment periods**\n**(i)**\nSubparagraphs (A) and (B) of section 51(i)(3) of such Code are each amended by striking subsection (a) and inserting subsection (a)(1) .\n**(ii)**\nSection 51(i)(3)(A) of such Code is amended by striking 40 percent and inserting 50 percent .\n##### (c) Removal of age limit for qualified supplemental nutrition assistance program benefits recipient\nSection 51(d)(8)(A)(i) of such Code is amended by striking but not age 40 .\n##### (d) Effective date\nThe amendments made by this section shall apply to individuals who begin work for the employer after December 31, 2025.\n#### 3. Eligibility of spouses of military personnel for the work opportunity credit\n##### (a) In general\nParagraph (1) of section 51(d) of the Internal Revenue Code of 1986 is amended by striking or at the end of subparagraph (I), by striking the period at the end of subparagraph (J) and inserting , or , and by adding at the end the following new subparagraph:\n(K) a qualified military spouse. .\n##### (b) Qualified military spouse\nSubsection (d) of section 51 of such Code is amended by adding at the end the following new paragraph:\n(16) Qualified military spouse The term qualified military spouse means any individual who is certified by the designated local agency as being (as of the hiring date) a spouse of a member of the Armed Forces of the United States. .\n##### (c) Effective date\nThe amendments made by this section shall apply to amounts paid or incurred after the date of the enactment of this Act to individuals who begin work for the employer after such date.\n#### 4. Promotion of targeted group member hiring to certain industries\nThe Secretary of the Treasury, the Secretary of Commerce, the Secretary of Labor, and the Administrator of the Small Business Administration (or their respective delegates), in consultation with each other and consistent with applicable law, shall promote the hiring of members of a targeted group (as defined in section 51(d) of the Internal Revenue Code of 1986) to business leaders across critical industry sectors, including manufacturing, infrastructure, energy, health care, and construction.",
      "versionDate": "2025-11-20",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-11-20",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "6231",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Improve and Enhance the Work Opportunity Tax Credit Act",
      "type": "HR"
    },
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
        "updateDate": "2026-01-06T15:56:55Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3265is.xml"
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
      "title": "Improve and Enhance the Work Opportunity Tax Credit Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-13T11:03:32Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Improve and Enhance the Work Opportunity Tax Credit Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-20T06:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to improve and enhance the work opportunity tax credit, to encourage longer-service employment, and to modernize the credit to make it more effective as a hiring incentive for targeted workers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-20T06:18:32Z"
    }
  ]
}
```
