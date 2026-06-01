# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3255?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3255
- Title: SWIFT Act
- Congress: 119
- Bill type: S
- Bill number: 3255
- Origin chamber: Senate
- Introduced date: 2025-11-20
- Update date: 2025-12-19T16:26:11Z
- Update date including text: 2025-12-19T16:26:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3255",
    "number": "3255",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "B001277",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Blumenthal, Richard [D-CT]",
        "lastName": "Blumenthal",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "SWIFT Act",
    "type": "S",
    "updateDate": "2025-12-19T16:26:11Z",
    "updateDateIncludingText": "2025-12-19T16:26:11Z"
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
        "item": {
          "date": "2025-11-20T19:10:10Z",
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
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "NY"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "MN"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "WA"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-11-20",
      "state": "VT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3255is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3255\nIN THE SENATE OF THE UNITED STATES\nNovember 20, 2025 Mr. Blumenthal (for himself, Mrs. Gillibrand , Ms. Klobuchar , Mrs. Murray , and Mr. Sanders ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title II of the Social Security Act to increase survivors benefits for disabled widows, widowers, and surviving divorced spouses, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Surviving Widow(er) Income Fair Treatment Act of 2025 or the SWIFT Act .\n#### 2. Eligibility for unreduced survivors benefits for widows, widowers, and surviving divorced spouses with disabilities at any age\n##### (a) In general\nSection 202 of the Social Security Act ( 42 U.S.C. 402 ) is amended\u2014\n**(1)**\nin subsection (e)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin subparagraph (B)(ii)\u2014\n**(I)**\nby striking has attained age 50 but has not attained age 60 and ; and\n**(II)**\nby striking which began before the end of the period specified in paragraph (4) ; and\n**(ii)**\nin subparagraph (F)(ii), by striking (I) in the period specified in paragraph (4) and (II) ;\n**(B)**\nby amending paragraph (3) to read as follows:\n(3) For purposes of paragraph (1), if a widow or surviving divorced wife marries after the first month in which she satisfies subparagraphs (A) and (B) of such paragraph, such marriage shall be deemed not to have occurred. ;\n**(C)**\nby striking paragraph (4); and\n**(D)**\nin paragraph (5)(A), by amending clause (ii) to read as follows:\n(ii) which begins not earlier than the first day of the seventeenth month before the month in which her application is filed. ; and\n**(2)**\nin subsection (f)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin subparagraph (B)(ii)\u2014\n**(I)**\nby striking has attained age 50 but has not attained age 60 and ; and\n**(II)**\nby striking which began before the end of the period specified in paragraph (4) ; and\n**(ii)**\nin subparagraph (F)(ii), by striking (I) in the period specified in paragraph (4) and (II) ;\n**(B)**\nby amending paragraph (3) to read as follows:\n(3) For purposes of paragraph (1), if a widower or surviving divorced husband marries after the first month in which he satisfies subparagraphs (A) and (B) of such paragraph, such marriage shall be deemed not to have occurred. ;\n**(C)**\nby striking paragraph (4); and\n**(D)**\nin paragraph (5)(A), by amending clause (ii) to read as follows:\n(ii) which begins not earlier than the first day of the seventeenth month before the month in which his application is filed. .\n##### (b) Elimination of reduction of benefit amounts for benefits claimed by widows, widowers, and surviving divorced spouses with disabilities before retirement age\nSection 202(q) of the Social Security Act ( 42 U.S.C. 402(q) ) is amended\u2014\n**(1)**\nin paragraph (3)(A), by striking and has attained age 62 and all that follows through widower's insurance benefit) and inserting and, in the case of a wife's or husband's insurance benefit, has attained age 62 ;\n**(2)**\nin paragraph (5), by adding at the end the following new subparagraph:\n(E) No widow's or widower's insurance benefit shall be reduced under this subsection for any month during which the individual entitled to such benefit is entitled to the benefit on the basis of paragraph (1)(B)(ii) of subsection (e) (in the case of a widow's insurance benefit) or paragraph (1)(B)(ii) of subsection (f) (in the case of a widower's insurance benefit). ; and\n**(3)**\nin paragraph (7)\u2014\n**(A)**\nin subparagraph (E), by striking benefits, and and inserting benefits, ;\n**(B)**\nin subparagraph (F), by striking the period at the end and inserting , and ; and\n**(C)**\nby adding at the end the following new subparagraph:\n(G) in the case of a widow's or widower's insurance benefit\u2014 (i) any month in which there was no reduction to the benefit under this subsection pursuant to paragraph (5)(E); and (ii) any month in which there would have been no reduction to the benefit under this subsection pursuant to paragraph (5)(E) if such paragraph had been in effect for such month. .\n##### (c) Technical and conforming amendments\n**(1) Social Security Act**\nTitle II of the Social Security Act ( 42 U.S.C. 401 et seq. ) is amended\u2014\n**(A)**\nin section 202\u2014\n**(i)**\nin subsection (e)\u2014\n**(I)**\nby redesignating paragraphs (5) through (8) as paragraphs (4) through (7); and\n**(II)**\nin paragraph (1)(F)(i), by striking (as defined in paragraph (5)) and inserting (as defined in paragraph (4)) ; and\n**(ii)**\nin subsection (f)\u2014\n**(I)**\nby redesignating paragraphs (5) through (8) as paragraphs (4) through (7); and\n**(II)**\nin paragraph (1)(F)(i), by striking (as defined in paragraph (5)) and inserting (as defined in paragraph (4)) ; and\n**(B)**\nin section 226(e)(1)(A), by striking thereof\u2014 and all that follows through (ii) the phrase and inserting thereof, the phrase .\n**(2) Railroad retirement Act**\nSection 4(g)(10)(i) of the Railroad Retirement Act of 1974 ( 42 U.S.C. 231c(g)(10)(i) ) is amended, in the second sentence, by striking 202(e)(7) and inserting 202(e)(6) .\n**(3) Federal Employees' Retirement System**\nSection 8442(f)(3)(A) of title 5, United States Code is amended, in the matter preceding clause (i), by striking 202(e)(7) and inserting 202(e)(6) .\n##### (d) Effective date\nThe amendments made by this section shall take effect on January 1, 2027, and shall apply to determinations of eligibility for, and the amount of, widow's and widower's insurance benefits payable on or after such date.\n#### 3. Increase in child's age limit for child-in-care benefits\n##### (a) In general\nSection 202(s)(1) of the Social Security Act ( 42 U.S.C. 402(s)(1) ) is amended by striking age of 16 and inserting age of 18 (or, in the case of a child who is a full-time elementary or secondary school student, 19) .\n##### (b) Effective date\nThe amendment made by this section shall take effect on January 1, 2027, and shall apply to determinations of eligibility for, and the amount of, benefits payable on or after such date.\n#### 4. Modification of benefit limit for widows, widowers, and surviving divorced spouses; increase in benefit amount for delay in claiming benefits\n##### (a) In general\nSection 202 of the Social Security Act ( 42 U.S.C. 402 ), as amended by section 2, is further amended\u2014\n**(1)**\nin subsection (e)(2)\u2014\n**(A)**\nin subparagraph (A), by inserting subsection (aa), subsection (bb) after subsection (q), ; and\n**(B)**\nby amending subparagraph (D) to read as follows:\n(D) Subject to subsections (aa) and (bb), if the deceased individual (on the basis of whose wages and self-employment income a widow or surviving divorced wife is entitled to widow's insurance benefits under this subsection) was, at any time, entitled to an old-age insurance benefit which was reduced by reason of the application of subsection (q), the widow's insurance benefit of such widow or surviving divorced wife for any month shall not exceed the greater of\u2014 (i) the amount of the old-age insurance benefit to which such deceased individual would have been entitled (after application of subsection (q)) for such month if such individual were still living and section 215(f)(5), 215(f)(6), or 215(f)(9)(B) were applied, where applicable; and (ii) 82 1/2 percent of the primary insurance amount (as determined without regard to subparagraph (C)) of such deceased individual. ;\n**(2)**\nin subsection (f)(2)\u2014\n**(A)**\nin subparagraph (A), by inserting subsection (aa), subsection (bb), after subsection (q), ; and\n**(B)**\nby amending subparagraph (D) to read as follows:\n(D) Subject to subsections (aa) and (bb), if the deceased individual (on the basis of whose wages and self-employment income a widower or surviving divorced husband is entitled to widower's insurance benefits under this subsection) was, at any time, entitled to an old-age insurance benefit which was reduced by reason of the application of subsection (q), the widower's insurance benefit of such widower or surviving divorced husband for any month shall not exceed the greater of\u2014 (i) the amount of the old-age insurance benefit to which such deceased individual would have been entitled (after application of subsection (q)) for such month if such individual were still living and section 215(f)(5), 215(f)(6), or 215(f)(9)(B) were applied, where applicable; and (ii) 82 1/2 percent of the primary insurance amount (as determined without regard to subparagraph (C)) of such deceased individual. ; and\n**(3)**\nby adding at the end the following new subsections:\n(aa) Increase over retirement insurance benefit limit of widow's and widower's insurance benefit amounts on account of delayed receipt of benefit (1) Subject to paragraph (6), the amount of a widow's or widower's insurance benefit (other than a benefit based on a primary insurance amount determined under section 215(a)(3) as in effect in December 1978 or section 215(a)(1)(C)(i) as in effect thereafter) which is payable without regard to this subsection to an individual who is described in paragraph (7) for a month shall be increased by\u2014 (A) the applicable percentage (as determined for the individual under paragraph (5)) of such amount, multiplied by (B) the number (if any) of the increment months for such individual. (2) For purposes of this subsection, the number of increment months for any individual shall be a number equal to the total number of months beginning on or after January 1, 2027, during which\u2014 (A) the individual\u2014 (i) would have been entitled to a widow's or widower's insurance benefit except that the individual had not filed an application for such benefit; or (ii) was entitled to a widow's or widower's insurance benefit that the individual did not receive pursuant to a request under subsection (z) that such benefit not be paid; (B) the individual had attained early retirement age (as defined in section 216(l)(2)); and (C) the individual was not under a penalty imposed under section 1129A. (3) For purposes of paragraph (1)(B), a determination of the total number of increment months for an individual shall be made each time the individual becomes entitled or re-entitled to a widow's or widower's insurance benefit or begins receiving such a benefit after a period during which the individual did not receive the benefit pursuant to a request under subsection (z) that such benefit not be paid. (4) This subsection shall be applied to a widow's or widower's insurance benefit before any reduction under this title except for the reduction under subparagraph (D) of subsection (e)(2) or (f)(2) (as applicable). (5) For purposes of paragraph (1)(A), the applicable percentage for an individual is a percentage equal to\u2014 (A) 28.5; divided by (B) the number of months between the month in which the individual attains early retirement age (as defined in section 216(l)(2)) and the month in which the individual attains retirement age (as defined in section 216(l)(1)). (6) In no case shall the amount of a widow or widower's insurance benefit be increased under this subsection to an amount that exceeds the higher of\u2014 (A) the primary insurance amount of the deceased individual on whose wages and self-employment income the widow's or widower's insurance benefit is based; or (B) the amount of the old-age insurance benefit to which such deceased individual would have been entitled (after application of subsection (q) and, where applicable, subsection (w)) for such month if such individual were still living and section 215(f)(5), 215(f)(6), or 215(f)(9)(B) were applied, where applicable. (7) An individual described in this section is an individual who is entitled to a widow's or widower's insurance benefit that is subject to reduction under subparagraph (D) of subsection (e)(2) or (f)(2) (as applicable). (bb) Increase in widow's and widower's insurance benefit amounts on account of delayed receipt of benefit (1) Subject to paragraph (6), the amount of a widow's or widower's insurance benefit (other than a benefit based on a primary insurance amount determined under section 215(a)(3) as in effect in December 1978 or section 215(a)(1)(C)(i) as in effect thereafter) which is payable without regard to this subsection to an individual for a month shall be increased by\u2014 (A) the applicable percentage (as determined for the individual under paragraph (5)) of such amount, multiplied by (B) the number (if any) of the increment months for such individual. (2) For purposes of this subsection, the number of increment months for any individual shall be a number equal to the total number of months beginning on or after January 1, 2027, during which\u2014 (A) the individual\u2014 (i) would have been entitled to a widow's or widower's insurance benefit except that the individual had not filed an application for such benefit; or (ii) was entitled to a widow's or widower's insurance benefit that the individual did not receive pursuant to a request under subsection (z) that such benefit not be paid; (B) the individual had attained retirement age (as defined in section 216(l)(1)); (C) the individual was not under a penalty imposed under section 1129A; and (D) the individual\u2014 (i) is not an individual described in subsection (aa)(7); or (ii) is an individual\u2014 (I) who is described in subsection (aa)(7); and (II) who, if the individual were entitled to and did receive a widower's or widower's insurance benefit for the month, would receive a benefit that would be increased under subsection (aa) to the maximum amount permissible under paragraph (6) of such subsection. (3) For purposes of paragraph (1), a determination of the total number of increment months for an individual shall be made each time the individual becomes entitled or re-entitled to a widow's or widower's insurance benefit or begins receiving such a benefit after a period during which the individual did not receive the benefit pursuant to a request under subsection (z) that such benefit not be paid. (4) This subsection shall be applied to a widow's or widower's insurance benefit\u2014 (A) after application of subsections (e)(2)(C), (f)(2)(C), and (aa) (as applicable); and (B) before any other reduction under this title. (5) For purposes of paragraph (1)(A), the applicable percentage for an individual is\u2014 (A) 1/12 of 1 percent in the case of an individual who attains early retirement age in any calendar year before 1979; (B) 1/4 of 1 percent in the case of an individual who attains early retirement age in any calendar year after 1978 and before 1987; (C) in the case of an individual who attains early retirement age in a calendar year after 1986 and before 2005, a percentage equal to the applicable percentage in effect under this subparagraph for persons who attain early retirement age in the preceding calendar year (as increased pursuant to this clause), plus 1/24 of 1 percent if the calendar year in which the individual involved attains early retirement age is not evenly divisible by 2; and (D) 2/3 of 1 percent in the case of an individual who attains early retirement age in a calendar year after 2004. (6) In no case shall the amount of a widow or widower's insurance benefit be increased under this subsection to an amount that exceeds the maximum amount to which the old age insurance benefit (as determined without regard to subsection (w)) of the individual on whose wages and self-employment income the widow's or widower's insurance benefit is based could have been increased under subsection (w). .\n##### (b) Conforming amendment\nSection 202(z)(1)(A) of the Social Security Act ( 42 U.S.C. 402(z)(1)(A) ) is amended\u2014\n**(1)**\nin the matter preceding clause (i), by inserting and any individual who is entitled to widow's or widower's insurance benefits at any age before may request that ; and\n**(2)**\nin clause (ii), by inserting , or, in the case of an individual entitled to a widow's or widower's insurance benefit, the first month in which, if the individual filed an application for such benefit or requested that such benefit be resumed in such month, the amount of such benefit would be equal to the maximum amount permissible under subsection (aa)(7) before the period.\n##### (c) Effective date\nThe amendments made by this section shall take effect on January 1, 2027, and shall apply to the determination of the amount of widow's and widower's insurance benefits payable on or after such date.\n#### 5. Holding current beneficiaries harmless\n##### (a) In general\nIn the case of an individual who is receiving benefits or assistance under any Federal program or under any State or local program financed in whole or in part with Federal funds as of the date on which the amendments made by this Act take effect, the amount of any additional income that is attributable to an increase in benefits under title II of the Social Security Act ( 42 U.S.C. 401 et seq. ) or to new eligibility for benefits under such title that results from the amendments made by this Act shall be disregarded for the purpose of determining such individual's continued eligibility for, and amount of, benefits or assistance under such Federal, State, or local program.\n##### (b) Limitation\nIn the case of an individual described in subsection (a) who, after the date on which the amendments made by this Act take effect, ceases to be eligible for benefits or assistance under a Federal, State, or local program described in such subsection, such subsection shall not apply to such individual for purposes of such program beginning on the date that such individual ceases to be so eligible.\n#### 6. Provision of information to widows, widowers, and surviving divorced spouses\n##### (a) In general\nNot later than January 1, 2027, the Commissioner of Social Security shall publish a booklet containing information related to benefits available under title II of the Social Security Act to widows, widowers, and surviving divorced spouses, including information on\u2014\n**(1)**\nhow old-age insurance benefits and survivors insurance benefits interact with each other;\n**(2)**\nhow to claim benefits, and how the timing of claiming benefits can impact benefit amounts;\n**(3)**\nthe lump sum death benefit; and\n**(4)**\nhow to contact the Social Security Administration for additional information.\n##### (b) Provision of booklet to widows, widowers, and surviving divorced spouses\nIn the case of any individual who dies on or after January 1, 2027, the Commissioner of Social Security shall, not later than 30 days after the Social Security Administration is informed of the death of such individual, mail a copy of the booklet described in subsection (a) to each widow, widower, or surviving divorced spouse of the individual who is known to the Social Security Administration (based on the records of the Social Security Administration).",
      "versionDate": "2025-11-20",
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
        "name": "Social Welfare",
        "updateDate": "2025-12-19T16:26:10Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3255is.xml"
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
      "title": "SWIFT Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-18T06:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SWIFT Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-18T06:38:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Surviving Widow(er) Income Fair Treatment Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-18T06:38:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title II of the Social Security Act to increase survivors benefits for disabled widows, widowers, and surviving divorced spouses, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-18T06:33:38Z"
    }
  ]
}
```
