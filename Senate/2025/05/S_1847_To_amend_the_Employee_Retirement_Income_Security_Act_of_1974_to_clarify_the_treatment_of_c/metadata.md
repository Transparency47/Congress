# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1847?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1847
- Title: Association Health Plans Act
- Congress: 119
- Bill type: S
- Bill number: 1847
- Origin chamber: Senate
- Introduced date: 2025-05-21
- Update date: 2026-04-13T14:50:17Z
- Update date including text: 2026-04-13T14:50:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-21: Introduced in Senate
- 2025-05-21 - IntroReferral: Introduced in Senate
- 2025-05-21 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-05-21: Introduced in Senate

## Actions

- 2025-05-21 - IntroReferral: Introduced in Senate
- 2025-05-21 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-21",
    "latestAction": {
      "actionDate": "2025-05-21",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1847",
    "number": "1847",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "P000603",
        "district": "",
        "firstName": "Rand",
        "fullName": "Sen. Paul, Rand [R-KY]",
        "lastName": "Paul",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "Association Health Plans Act",
    "type": "S",
    "updateDate": "2026-04-13T14:50:17Z",
    "updateDateIncludingText": "2026-04-13T14:50:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-21",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-21",
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
            "date": "2025-05-21T20:35:28Z",
            "name": "Referred To"
          },
          {
            "date": "2025-05-21T20:35:28Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-05-21",
      "state": "MS"
    },
    {
      "bioguideId": "S001184",
      "firstName": "Tim",
      "fullName": "Sen. Scott, Tim [R-SC]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "SC"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-10-16",
      "state": "FL"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "FL"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1847is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1847\nIN THE SENATE OF THE UNITED STATES\nMay 21, 2025 Mr. Paul (for himself and Mr. Wicker ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Employee Retirement Income Security Act of 1974 to clarify the treatment of certain association health plans as employers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Association Health Plans Act .\n#### 2. Treatment of group or association of employers\n##### (a) In general\nSection 3(5) of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1002(5) ) is amended\u2014\n**(1)**\nby striking The term and inserting (A) The term ; and\n**(2)**\nby adding at the end the following:\n(B) For purposes of subparagraph (A), a group or association of employers shall be treated as an employer , regardless of whether the employers composing such group or association are in the same industry, trade, or profession, if such group or association\u2014 (i) (I) has established and maintains an employee welfare benefit plan that is a group health plan (as defined in section 733(a)(1)); (II) provides coverage under such plan to at least 51 employees after all of the employees employed by all of the employer members of such group or association have been aggregated and counted together as described in subparagraph (D); (III) has been actively in existence for at least 2 years; (IV) has been formed and maintained in good faith for purposes other than providing medical care (as defined in section 733(a)(2)) through the purchase of insurance or otherwise; (V) does not condition membership in the group or association on any health status-related factor (as described in section 702(a)(1)) relating to any individual; (VI) makes coverage under such plan available to all employer members of such group or association regardless of any health status-related factor (as described in section 702(a)(1)) relating to such employer members; (VII) does not provide coverage under such plan to any individual other than an employee of an employer member of such group or association; (VIII) has established a governing board with by-laws or other similar indications of formality to manage and operate such plan in both form and substance, of which at least 75 percent of the board members shall be made up of employer members of such group or association participating in the plan that are duly elected by each participating employer member casting 1 vote during a scheduled election; (IX) is not a health insurance issuer (as defined in section 733(b)(2)), and is not owned or controlled by such a health insurance issuer or by a subsidiary or affiliate of such a health insurance issuer, other than to the extent such a health insurance issuer may participate in the group or association as a member; (ii) is structured in good faith with any set of criteria to qualify for such treatment in any advisory opinion issued prior to the date of enactment of the Association Health Plans Act ; or (iii) meets any other set of criteria to qualify for such treatment that the Secretary by regulation may provide. (C) (i) For purposes of subparagraph (B), a self-employed individual shall be treated as\u2014 (I) an employer who may become a member of a group or association of employers; (II) an employee who may participate in an employee welfare benefit plan established and maintained by such group or association; and (III) a participant of such plan subject to the eligibility determination and monitoring requirements set forth in clause (iii). (ii) For purposes of this subparagraph, the term self-employed individual means an individual who\u2014 (I) does not have any common law employees; (II) has a bona fide ownership right in a trade or business, regardless of whether such trade or business is incorporated or unincorporated; (III) earns wages (as defined in section 3121(a) of the Internal Revenue Code of 1986) or self-employment income (as defined in section 1402(b) of such Code) from such trade or business; and (IV) works at least 10 hours a week or 40 hours per month providing personal services to such trade or business. (iii) The board of a group or association of employers shall\u2014 (I) initially determine whether an individual meets the requirements under clause (ii) to be considered to a self-employed individual for the purposes of being treated as an\u2014 (aa) employer member of such group or association (in accordance with clause (i)(I)); and (bb) employee who may participate in the employee welfare benefit plan established and maintained by such group or association (in accordance with clause (i)(II)); (II) through reasonable monitoring procedures, periodically determine whether the individual continues to meet such requirements; and (III) if the board determines that an individual no longer meets such requirements, not make such plan coverage available to such individual (or dependents thereof) for any plan year following the plan year during which the board makes such determination. If, subsequent to a determination that an individual no longer meets such requirements, such individual furnishes evidence of satisfying such requirements, such individual (and dependents thereof) shall be eligible to receive plan coverage. (D) For purposes of subparagraph (B), all of the employees (including self-employed individuals) employed by all of the employer members (including self-employed individuals) of a group or association of employers shall be\u2014 (i) treated as participants in a single plan multiple employer welfare arrangement; and (ii) aggregated and counted together for purposes of any regulation of an employee welfare benefit plan established and maintained by such group or association. .\n##### (b) Determination of employer or joint employer status\nThe provision of employee welfare benefit plan coverage by a group or association of employers shall not be construed as evidence for establishing an employer or joint employer relationship under any Federal or State law.\n#### 3. Rules applicable to employee welfare benefit plans established and maintained by a group or association of employers\nPart 7 of subtitle B of title I of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1181 et seq. ) is amended by adding at the end the following:\n736. Rules applicable to employee welfare benefit plans established and maintained by a group or association of employers (a) Premium rates for a group or association of employers (1) (A) In the case of an employee welfare benefit plan established and maintained by a group or association of employers described in section 3(5)(B), such plan may, to the extent not prohibited under State law\u2014 (i) establish base premium rates formed on an actuarially sound, modified community rating methodology that considers the pooling of all plan participant claims; and (ii) utilize the specific risk profile of each employer member of such group or association to determine contribution rates for each such employer member\u2019s share of a premium by actuarially adjusting above or below the established base premium rates. (B) For purposes of paragraph (1), the term employer member means\u2014 (i) an employer who is a member of such group or association of employers and employs at least 1 common law employee; or (ii) a group made up solely of self-employed individuals, within which all of the self-employed individual members of such group or association are aggregated together as a single employer member group, provided the group includes at least 20 self-employed individual members. (2) In the event a group or association is made up solely of self-employed individuals (and no employers with at least 1 common law employee are members of such group or association), the employee welfare benefit plan established by such group or association shall\u2014 (A) treat all self-employed individuals who are members of such group or association as a single risk pool; (B) pool all plan participant claims; and (C) charge each plan participant the same premium rate. (b) Discrimination and pre-Existing condition protections An employee welfare benefit plan established and maintained by a group or association of employers described in section 3(5)(B) shall be prohibited from\u2014 (1) establishing any rule for eligibility (including continued eligibility) of any individual (including an employee of an employer member or a self-employed individual, or a dependent of such employee or self-employed individual) to enroll for benefits under the terms of the plan that discriminates based on any health status-related factor that relates to such individual (consistent with the rules under section 702(a)(1)); (2) requiring an individual (including an employee of an employer member or a self-employed individual, or a dependent of such employee or self-employed individual), as a condition of enrollment or continued enrollment under the plan, to pay a premium or contribution that is greater than the premium or contribution for a similarly situated individual enrolled in the plan based on any health status-related factor that relates to such individual (consistent with the rules under section 702(b)(1)); and (3) denying coverage under such plan on the basis of a pre-existing condition (consistent with the rules under section 2704 of the Public Health Service Act). .\n#### 4. Rule of construction\nNothing in this Act shall be construed to exempt a group health plan which is an employee welfare benefit plan offered through a group or association of employers from the requirements of part 7 of subtitle B of title I of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1181 et seq. ), including the provisions of part A of title XXVII of the Public Health Service Act as incorporated by reference into this Act through section 715.",
      "versionDate": "2025-05-21",
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
        "actionDate": "2025-12-15",
        "text": "Placed on the Union Calendar, Calendar No. 357."
      },
      "number": "2528",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Association Health Plans Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Disability and health-based discrimination",
            "updateDate": "2025-06-27T17:22:27Z"
          },
          {
            "name": "Employee benefits and pensions",
            "updateDate": "2025-06-27T17:22:27Z"
          },
          {
            "name": "Health care costs and insurance",
            "updateDate": "2025-06-27T17:22:27Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-06-27T17:22:27Z"
          },
          {
            "name": "Labor-management relations",
            "updateDate": "2025-06-27T17:22:27Z"
          },
          {
            "name": "Self-employed",
            "updateDate": "2025-06-27T17:22:27Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-06-16T13:07:16Z"
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
      "date": "2025-05-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1847is.xml"
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
      "title": "Association Health Plans Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-12T12:03:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Association Health Plans Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-04T03:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Employee Retirement Income Security Act of 1974 to clarify the treatment of certain association health plans as employers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-04T03:18:38Z"
    }
  ]
}
```
