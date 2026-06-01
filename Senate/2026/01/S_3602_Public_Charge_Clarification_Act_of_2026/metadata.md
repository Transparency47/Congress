# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3602?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3602
- Title: Public Charge Clarification Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3602
- Origin chamber: Senate
- Introduced date: 2026-01-08
- Update date: 2026-02-05T16:25:06Z
- Update date including text: 2026-02-05T16:25:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-08: Introduced in Senate
- 2026-01-08 - IntroReferral: Introduced in Senate
- 2026-01-08 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-01-08: Introduced in Senate

## Actions

- 2026-01-08 - IntroReferral: Introduced in Senate
- 2026-01-08 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-08",
    "latestAction": {
      "actionDate": "2026-01-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3602",
    "number": "3602",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "M001198",
        "district": "",
        "firstName": "Roger",
        "fullName": "Sen. Marshall, Roger [R-KS]",
        "lastName": "Marshall",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "Public Charge Clarification Act of 2026",
    "type": "S",
    "updateDate": "2026-02-05T16:25:06Z",
    "updateDateIncludingText": "2026-02-05T16:25:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-08",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-01-08",
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
          "date": "2026-01-08T17:54:43Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2026-01-08",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3602is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3602\nIN THE SENATE OF THE UNITED STATES\nJanuary 8 (legislative day, January 7), 2026 Mr. Marshall (for himself and Mr. Scott of Florida ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend the Immigration and Nationality Act to clarify the definitions of public charge and likely at any time to become a public charge, to establish requirements for affidavits of support and public charge bonds, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Public Charge Clarification Act of 2026 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nSection 212(a)(4)(A) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a)(4)(A) ) establishes that an alien who, in the opinion of the consular officer or the Director of U.S. Citizenship and Immigration Services, is likely at any time to become a public charge is inadmissible.\n**(2)**\nIn section 212(a)(4)(B) of such Act, Congress laid out specific factors to be considered in determining whether an alien is likely to become a public charge, including the alien\u2019s age, health, family status, assets, resources, financial status, education, and skills, and any affidavit of support executed by a sponsor of such alien in accordance with section 213A(a)(1) of such Act ( 8 U.S.C. 1183a(a)(1) ).\n**(3)**\nThese statutory factors have not been faithfully applied in the intended totality of the circumstances analysis by executive agencies, which has resulted in inconsistent and overly permissive interpretations that undermine congressional intent to ensure self-sufficiency among new immigrants.\n**(4)**\nThe proposed rule entitled Inadmissibility on Public Charge Grounds (83 Fed. Reg. 51114), which was published in the Federal Register by U.S. Citizenship and Immigration Services on October 10, 2018, provided a clear framework for identifying public benefits that render an alien a public charge, including both monetizable and non-monetizable benefits.\n**(5)**\nTo protect American taxpayers and promote immigrant self-sufficiency, it is necessary to codify and expand upon this framework, ensuring that all current and future government benefits are considered in public charge determinations.\n#### 3. Definition of public charge\nSection 212(a)(4) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a)(4) ) is amended to read as follows:\n(4) Public charge (A) In general Any alien who, in the opinion of the consular officer at the time of application for a visa, or in the opinion of the Attorney General at the time of application for admission or adjustment of status, is likely at any time to become a public charge is inadmissible. (B) Definitions In this paragraph: (i) Likely at any time to become a public charge The term likely at any time to become a public charge , with respect to an alien, means the alien is likely to receive 1 or more public benefits for more than 12 months, in the aggregate, during any 36-month period after the date on which\u2014 (I) the alien is admitted to the United States; or (II) the alien's status is adjusted under this title. (ii) Public benefits The term public benefits means any Federal, State, local, or tribal cash assistance for income maintenance, supplemental nutrition assistance, housing assistance, non-emergency medical assistance, or other similar benefits, including all monetizable and non-monetizable benefits (as defined in the proposed rule entitled Inadmissibility on Public Charge Grounds, (83 Fed. Reg. 51114)), including benefits received from\u2014 (I) supplemental security income authorized under title XVI of the Social Security Act ( 42 U.S.C. 1381 et seq. ); (II) temporary assistance for needy families authorized under part A of title IV of such Act ( 42 U.S.C. 601 et seq. ); (III) any Federal, State, local, or tribal cash benefit program for income maintenance; (IV) the supplemental nutrition assistance program authorized under the Food and Nutrition Act of 2008 ( 7 U.S.C. 2011 et seq. ); (V) the housing choice voucher program and project-based rental assistance (including moderate rehabilitation) authorized under section 8 of the United States Housing Act of 1937 ( 42 U.S.C. 1437f ); (VI) public housing funds authorized under section 9 of such Act ( 42 U.S.C. 1437g ); (VII) the Medicaid program authorized under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ), excluding emergency medical assistance, benefits provided to individuals who are younger than 21 years of age, and benefits provided to pregnant women; (VIII) premium and cost-sharing subsidies authorized under section 36B of the Internal Revenue Code of 1986 (relating to refundable credit for coverage under a qualified health plan) or section 1402 of the Patient Protection and Affordable Care Act ( 14 U.S.C. 18071 ; relating to reduced cost sharing); and (IX) any other Federal, State, local, or tribal program providing monetizable or non-monetizable benefits, including programs established after the date of the enactment of the Public Charge Clarification Act of 2026 . (iii) Public charge The term public charge means an alien who receives 1 or more public benefits for more than 12 months, in the aggregate, within any 36-month period. The receipt of 2 benefits in a single month shall be deemed to constitute 2 months of benefits for purposes of this clause. (C) Publication of list of benefits (i) In general Not later than 180 days after the date of enactment of the Public Charge Clarification Act of 2026 , the Secretary of Homeland Security, acting through the Director of U.S. Citizenship and Immigration Services, shall publish in the Federal Register a comprehensive list of all public benefits that may render an alien a public charge or likely to become a public charge. (ii) Updates The Secretary shall\u2014 (I) update the list described in clause (i) whenever necessary to include any new programs or benefits created after the publication of such list; and (II) publish notice of such updates in the Federal Register. (D) Factors to be considered (i) In general In determining whether an alien is inadmissible under this paragraph, the consular officer or the Director of U.S. Citizenship and Immigration Services shall consider, in the totality of the circumstances, the alien\u2019s\u2014 (I) age; (II) health; (III) family status; (IV) assets, resources, and financial status; (V) education and skills; (VI) prospective immigration status and expected period of admission; and (VII) any affidavit of support executed by a sponsor in accordance with section 213A(a)(1). (ii) Determination No single factor listed under clause (i) shall be dispositive. The determination of inadmissibility shall be based on a holistic assessment of the alien\u2019s likelihood of becoming a public charge. (E) Exemptions This paragraph shall not apply to\u2014 (i) refugees admitted under section 207; (ii) asylees granted asylum under section 208; or (iii) aliens serving in the Armed Forces of the United States and the dependents of such aliens. (F) Waivers No waiver of inadmissibility under this paragraph shall be granted to any alien, other than the aliens exempted under subparagraph (F), unless such waiver is specifically authorized by an Act of Congress. (G) Affidavits of support An affidavit of support submitted by the sponsor of an alien in accordance with section 213A\u2014 (i) shall be accompanied by documentary evidence demonstrating the sponsor\u2019s ability to financially support the alien and all members of the sponsor\u2019s household, including proof of income, assets, and resources sufficient to maintain the household at an annual income equal to at least 125 percent of the Federal poverty line; and (ii) may be considered as a factor in the totality of the circumstances under subparagraph (D), but shall not be sufficient to overcome a finding that an alien is likely to become a public charge. (H) Public charge bonds (i) Requirement The consular officer or the Director of U.S. Citizenship and Immigration Services shall require the posting of a public charge bond as a condition of an alien's admission or adjustment of status if the alien is likely at any time to become a public charge, but other factors warrant conditional approval. (ii) Amount; forfeiture Each public charge bond required under clause (i) shall be\u2014 (I) in an amount equal to not less than $10,000; (II) payable to the United States; and (III) forfeited if the alien for whom it is posted becomes a public charge during the 10-year period immediately following the alien's admission to the United States or adjustment of status. (iii) Rulemaking The Secretary of Homeland Security, in consultation with the Director of U.S. Citizenship and Immigration Services, shall promulgate regulations for the administration, forfeiture, and cancellation of public charge bonds required under this subparagraph. .\n#### 4. Conforming amendments\n##### (a) Immigration and Nationality Act\nSection 213A of the Immigration and Nationality Act ( 8 U.S.C. 1183a ) is amended\u2014\n**(1)**\nby redesignating subsections (h) and (i) as subsections (g) and (h), respectively; and\n**(2)**\nby adding at the end the following:\n(i) Requirements for public charge determinations Affidavits of support under this section shall comply with the requirements set forth in section 212(a)(4)(G). .\n##### (b) Other laws\nAny reference in any Federal law or regulation to public charge or likely to become a public charge shall be construed in accordance with the amendments made by section 3.\n#### 5. Effective date\nThe amendments made by this Act shall\u2014\n**(1)**\ntake effect on the date that is 180 days after the date of the enactment of this Act; and\n**(2)**\napply to all applications for visas, admission, or adjustment of status pending on, or filed after, such effective date.",
      "versionDate": "2026-01-08",
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
        "name": "Immigration",
        "updateDate": "2026-02-05T16:25:06Z"
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
      "date": "2026-01-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3602is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Immigration and Nationality Act to clarify the definitions of \"public charge\" and \"likely at any time to become a public charge,\" to establish requirements for affidavits of support and public charge bonds, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-03T11:03:34Z"
    },
    {
      "title": "Public Charge Clarification Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-03T10:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Public Charge Clarification Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-03T10:53:14Z"
    }
  ]
}
```
