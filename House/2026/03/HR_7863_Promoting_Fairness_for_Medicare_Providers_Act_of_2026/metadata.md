# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7863?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7863
- Title: Promoting Fairness for Medicare Providers Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7863
- Origin chamber: House
- Introduced date: 2026-03-09
- Update date: 2026-04-02T18:31:34Z
- Update date including text: 2026-04-02T18:31:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-09: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-09 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-03-09: Introduced in House

## Actions

- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-09 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-09",
    "latestAction": {
      "actionDate": "2026-03-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7863",
    "number": "7863",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001257",
        "district": "12",
        "firstName": "Gus",
        "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
        "lastName": "Bilirakis",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Promoting Fairness for Medicare Providers Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-02T18:31:34Z",
    "updateDateIncludingText": "2026-04-02T18:31:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-09",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-09",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-09",
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
          "date": "2026-03-09T17:02:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-03-09T17:02:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "R000599",
      "district": "25",
      "firstName": "Raul",
      "fullName": "Rep. Ruiz, Raul [D-CA-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Ruiz",
      "party": "D",
      "sponsorshipDate": "2026-03-09",
      "state": "CA"
    },
    {
      "bioguideId": "M001210",
      "district": "3",
      "firstName": "Gregory",
      "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2026-03-09",
      "state": "NC"
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
      "sponsorshipDate": "2026-03-09",
      "state": "IL"
    },
    {
      "bioguideId": "J000302",
      "district": "13",
      "firstName": "John",
      "fullName": "Rep. Joyce, John [R-PA-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Joyce",
      "party": "R",
      "sponsorshipDate": "2026-03-17",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7863ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7863\nIN THE HOUSE OF REPRESENTATIVES\nMarch 9, 2026 Mr. Bilirakis (for himself, Mr. Ruiz , Mr. Murphy , and Mr. Davis of Illinois ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to align payment under Medicare for specified surgical procedures with high-cost supplies furnished in office-based facilities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Promoting Fairness for Medicare Providers Act of 2026 .\n#### 2. Aligning payment under medicare for specified high supply cost surgical procedures furnished in office-based facilities\n##### (a) Coverage of facility services\nSection 1832(a)(2)(F) of the Social Security Act ( 42 U.S.C. 1395k(a)(2)(F) ) is amended\u2014\n**(1)**\nin the matter preceding clause (i), by striking specified by the Secretary ;\n**(2)**\nin clause (i)\u2014\n**(A)**\nby inserting specified by the Secretary before pursuant ; and\n**(B)**\nat the end, by striking or ;\n**(3)**\nin clause (ii)\u2014\n**(A)**\nby inserting specified by the Secretary before pursuant ; and\n**(B)**\nat the end, by striking the semicolon and inserting , or ; and\n**(4)**\nby adding at the end the following new clause:\n(iii) that are specified high supply cost surgical procedures (as defined in section 1834(bb)(4) with respect to a year (beginning with 2027) and furnished during such year in an office-based facility (as defined in section 1834(bb)(5)); .\n##### (b) Payment rules\n**(1) Payment for facility services**\nSection 1833(a)(1) of the Social Security Act ( 42 U.S.C. 1395l(a) ) is amended\u2014\n**(A)**\nby striking and (HH) and inserting (HH) ; and\n**(B)**\nby inserting before the semicolon at the end the following , and (II) with respect to facility services furnished in connection with a specified high supply cost surgical procedure (as defined in section 1834(bb)(4)) with respect to a year (beginning with 2027) furnished to an individual in an office-based facility (as defined in section 1834(bb)(5)) during such year, the amounts paid shall be, subject to section 1834(bb)(3), 80 percent of the payment amount determined under section 1834(bb) for such facility services furnished in connection with such procedure at such office-based facility .\n**(2) Payment determination for specified high supply cost surgical procedures furnished in office-based facilities**\nSection 1834 of the Social Security Act ( 42 U.S.C. 1395l(a) ) is amended by adding at the end the following new subsection:\n(bb) Payment for specified high supply cost surgical procedures furnished in office-Based facilities (1) In general In the case of a specified high supply cost surgical procedure furnished in an office-based facility during 2027 or a subsequent year, subject to paragraphs (2) and (3), payment for such procedure shall be determined under this part in the same manner as payment would be determined under this part if such procedure had been furnished in an ambulatory surgical center and not considered office-based under section 1833(i)(1)(B), except that payment for facility services furnished in connection with such procedure shall be equal to 90 percent of the amount that would be payable for facility services furnished in connection with such procedure under section 1833(i) for such year if such procedure had been furnished in an ambulatory surgical center and treated as a service commonly furnished in such a center. (2) Application in case of device-intensive procedures In applying paragraph (1) in the case of a specified high supply cost surgical procedure that is a device-intensive procedure (as described in section 416.171(b)(2) of title 42, Code of Federal Regulations (or any successor regulation)), instead of the payment amount applied under such paragraph, the payment amount for the facility services with respect to such procedure shall be the amount that would be calculated under section 416.172(h)(2)(ii) of title 42, Code of Federal Regulations (or any successor regulation) with respect to a procedure that has been assigned device-intensive status, except that in applying such calculation the non-device portion described in paragraph (B) of such section shall be equal to 90 percent of the amount that would otherwise be calculated for such portion. (3) Limitation on copayment amount to inpatient hospital deductible amount (A) In general In no case shall the amount of coinsurance for facility services furnished in connection with a specified high supply cost surgical procedure in an office-based facility during a year exceed the amount of the inpatient hospital deductible established under section 1813(b) for that year. (B) Maintaining payment to provider In the case that an individual enrolled under this part would, without application of subparagraph (A), be subject to an amount of coinsurance for facility services furnished in connection with a specified high supply cost surgical procedure in an office-based facility during a year that exceeds the amount of the inpatient hospital deductible established under section 1813(b) for that year, the Secretary shall increase the amount paid to the office-based facility as specified under section 1833(a)(1)(II) for such facility services by the amount by which\u2014 (i) the coinsurance payable by the individual for such facility services without application of this paragraph; exceeds (ii) the coinsurance payable by the individual for such facility services with application of this paragraph. (4) Specified high supply cost surgical procedure defined (A) In general For purposes of this part, subject to subparagraphs (B) and (C), the term specified high supply cost surgical procedure means a surgical procedure that as of 2023\u2014 (i) when performed in an ambulatory surgical center, was payable under section 1833(i); and (ii) when performed in a physician\u2019s office\u2014 (I) was payable under section 1848 at the practice expense relative value unit-based amount for non-facility sites of service; and (II) included a HCPCS code with a supply item for which the price input for such supply item, used for determining the practice expense relative value units for such code, was greater than $500. (B) Review and revisions to specified services (i) In general For each year (beginning with 2028), the Secretary shall review the procedures included in the definition of specified high supply cost surgical procedures under this paragraph and, based on such review and through rulemaking\u2014 (I) shall add a surgical procedure (not described in subparagraph (A)) for inclusion in such definition if the procedure, with respect to such year, satisfies the criteria specified in clause (ii); and (II) may remove a surgical procedure from inclusion in such definition if the procedure, with respect to such year, satisfies the criteria specified in clause (iii). (ii) Criteria for required inclusion For purposes of clause (i)(I), a surgical procedure satisfies the criteria specified in this clause, with respect to a year, if\u2014 (I) when performed in an ambulatory surgical center, the procedure is payable under section 1833(i); and (II) when performed in a physician\u2019s office, the procedure\u2014 (aa) would be, without application of this subsection or section 1833(a)(i)(II), payable under section 1848 at the practice expense relative value unit-based amount for non-facility sites of services; and (bb) includes a HCPCS code with a supply item for which the price input for such supply item, used for determining the practice expense relative value units for such code, is greater than the threshold specified in clause (iv) for such year. (iii) Criteria for permissive removal For purposes of clause (i)(II), a surgical procedure satisfies the criteria described in this clause, with respect to a year, if, when performed in a physician\u2019s office, the procedure includes a HCPCS code with a supply item for which the price input for such supply item, used for determining the practice expense relative value units for such code, does not exceed the amount equal to 80 percent of the threshold specified in clause (iv) for such year. (iv) Dollar amount threshold specified For purposes of clauses (ii) and (iii), the threshold specified in this clause is\u2014 (I) with respect to 2028, the dollar amount specified in subparagraph (A)(ii), reduced by the percentage increase in the MEI (as defined in section 1842(i)(3)) over the 3-year period ending with 2028; or (II) with respect to a subsequent year, the amount specified in this clause for the preceding year reduced by the percentage increase in the MEI (as defined in section 1842(i)(3)) for such subsequent year. (C) Special rule for use of more than one of the same supply item in a procedure In the case of a surgical procedure that requires the use of more than one of the same supply item in such procedure\u2014 (i) in applying subparagraph (A)(ii)(II), if as of 2023 the sum of the price inputs described in such subparagraph of all of such same supply items exceeds the dollar amount specified in such subparagraph, then the procedure shall be treated as satisfying the requirement of such subparagraph; and (ii) in applying subparagraph (B), with respect to 2028 or a subsequent year\u2014 (I) if the sum of the price inputs described in clause (ii)(II)(bb) of such subparagraph of all of such same supply items exceeds the threshold specified in clause (iv) of such subparagraph for such year, then the procedure shall be treated as satisfying the criterion described in such clause (ii)(II)(bb) with respect to such year; and (II) if the sum of the price inputs described in clause (iii) of such subparagraph of all of such same supply items does not exceed the amount described in such clause for such year, then the procedure shall be treated as satisfying the criteria described in such clause with respect to such year. (5) Office-based facility defined For purposes of this part, the term office-based facility means a physician\u2019s office that, with respect to facility services furnished in connection with specified high supply cost surgical procedures\u2014 (A) meets health, safety, and other standards specified by the Secretary in regulations; and (B) has entered into an agreement with the Secretary under which the physician\u2019s office\u2014 (i) accepts the payment amount determined under this subsection as full payment for such facility services; (ii) accepts an assignment described in section 1842(b)(3)(B)(ii) with respect to payment for all such facility services furnished by the office to individuals enrolled under this part; and (iii) participates under this part and is paid as an office-based facility with respect to all such procedures. .\n**(3) Conforming amendments**\n**(A) For services furnished in an ambulatory surgical center**\nSection 1833(i)(2) of the Social Security Act ( 42 U.S.C. 1395l(i)(2) ) is amended by adding at the end the following new subparagraph:\n(F) For purposes of determining payment under this subsection for a specified high supply cost surgical procedure (as defined in section 1834(bb)(4) with respect to a year (beginning with 2027)) furnished in an ambulatory surgical center during such year, such procedure shall be treated as a service commonly furnished in an ambulatory surgical center. .\n**(B) For services furnished in an off-campus outpatient department of a provider**\nSection 1833(t)(21)(C) of the Social Security Act ( 42 U.S.C. 1395l(t)(21)(C) ) is amended by adding at the end the following new sentence: In applying the previous sentence in the case of a specified high supply cost surgical procedure (as defined in section 1834(bb)(4) with respect to a year) furnished by an off-campus outpatient department of a provider, payment shall be determined under section 1834(bb). .\n**(C) For clarification on applicable payment for obf facility services**\nSection 1833(a)(4) of the Social Security Act ( 42 U.S.C. 1395l(a)(4) ) is amended by inserting (other than in clause (iii) of such section) after section 1832(a)(2)(F) .\n##### (c) Provider agreement and medicare enrollment\n**(1) In general**\nSection 1866(e) of the Social Security Act ( 42 U.S.C. 1395cc(e) ) is amended\u2014\n**(A)**\nin paragraph (2), by striking at the end and ;\n**(B)**\nin paragraph (3), at the end, by striking the period and adding ; and ; and\n**(C)**\nby adding at the end the following new paragraph:\n(4) an office-based facility (as defined in paragraph (5) of section 1834(bb)), but only with respect to the furnishing during a year of specified high supply cost surgical procedures (as defined in paragraph (4) of such section with respect to such year). .\n**(2) Consultation with state agencies regarding conditions of participation**\nSection 1863 of the Social Security Act ( 42 U.S.C. 1395z ) is amended by striking or by ambulatory surgical centers under section 1832(a)(2)(F)(i) and inserting by ambulatory surgical centers under section 1832(a)(2)(F)(i), or by office-based facilities (as defined in section 1834(bb)(5)) with respect to furnishing specified high supply cost surgical procedures (as defined in section 1834(bb)(4)) .\n**(3) Use of state agencies to determine compliance with conditions of participation**\nSection 1864(a) of the Social Security Act ( 42 U.S.C. 1395aa(a) ) is amended\u2014\n**(A)**\nin the first sentence, by inserting or whether a physician\u2019s office is an office-based facility (as defined in section 1834(bb)(5), after standards specified under section 1832(a)(2)(F)(i), ; and\n**(B)**\nin the fifth sentence, by inserting office-based facility (as defined in section 1834(bb)(5)) with respect to furnishing ambulatory high supply cost surgical procedures (as defined in section 1834(bb)(4)), after each occurrence of ambulatory surgical center, .",
      "versionDate": "2026-03-09",
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
        "name": "Health",
        "updateDate": "2026-04-02T18:31:34Z"
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
      "date": "2026-03-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7863ih.xml"
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
      "title": "Promoting Fairness for Medicare Providers Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-26T03:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Promoting Fairness for Medicare Providers Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-26T03:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to align payment under Medicare for specified surgical procedures with high-cost supplies furnished in office-based facilities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-26T03:03:30Z"
    }
  ]
}
```
