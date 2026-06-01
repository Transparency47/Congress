# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2886?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2886
- Title: America’s CHILDREN Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2886
- Origin chamber: Senate
- Introduced date: 2025-09-18
- Update date: 2026-02-04T12:03:15Z
- Update date including text: 2026-02-04T12:03:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-18: Introduced in Senate
- 2025-09-18 - IntroReferral: Introduced in Senate
- 2025-09-18 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-09-18: Introduced in Senate

## Actions

- 2025-09-18 - IntroReferral: Introduced in Senate
- 2025-09-18 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-18",
    "latestAction": {
      "actionDate": "2025-09-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2886",
    "number": "2886",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "P000145",
        "district": "",
        "firstName": "Alex",
        "fullName": "Sen. Padilla, Alex [D-CA]",
        "lastName": "Padilla",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "America\u2019s CHILDREN Act of 2025",
    "type": "S",
    "updateDate": "2026-02-04T12:03:15Z",
    "updateDateIncludingText": "2026-02-04T12:03:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-18",
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
      "actionDate": "2025-09-18",
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
            "date": "2025-09-18T19:23:05Z",
            "name": "Referred To"
          },
          {
            "date": "2025-09-18T19:23:05Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "P000603",
      "firstName": "Rand",
      "fullName": "Sen. Paul, Rand [R-KY]",
      "isOriginalCosponsor": "True",
      "lastName": "Paul",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "KY"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "IL"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "ME"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "MN"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "AK"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "DE"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "ND"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-09-18",
      "state": "ME"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "UT"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "IA"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2886is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2886\nIN THE SENATE OF THE UNITED STATES\nSeptember 18 (legislative day, September 16), 2025 Mr. Padilla (for himself, Mr. Paul , Mr. Durbin , Ms. Collins , Ms. Klobuchar , Ms. Murkowski , Mr. Coons , Mr. Cramer , Mr. King , and Mr. Curtis ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend the Immigration and Nationality Act to authorize lawful permanent resident status for certain college graduates who entered the United States as children, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the America\u2019s CHILDREN Act of 2025 or the Protecting Children of Long-Term Visa Holders Act of 2025 .\n#### 2. Permanent resident status for certain college graduates who entered the United States as children\n##### (a) Requirements\nSection 201(b)(1) of the Immigration and Nationality Act ( 8 U.S.C. 1151(b)(1) ) is amended by adding at the end the following:\n(F) Any alien who\u2014 (i) is not inadmissible under section 212(a) or deportable under section 237(a); (ii) was lawfully present in the United States as a dependent child of a nonimmigrant admitted to engage in employment in the United States (other than a nonimmigrant described in subparagraph (A), (G), (N), or (S) of section 101(a)(15)) for an aggregate period of not less than 8 years; (iii) on the date on which an application under section 204(a)(1)(M) is submitted, has been lawfully present in the United States for an aggregate period of not less than 10 years; and (iv) has graduated from an institution of higher education (as defined in section 102(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1002(a) )) in the United States. .\n##### (b) Petition\nSection 204(a)(1) of the Immigration and Nationality Act ( 8 U.S.C. 1154(a)(1) ) is amended by adding at the end the following:\n(M) Any alien entitled to classification under section 201(b)(1)(F) may file a petition with the Secretary of Homeland Security for such classification. .\n#### 3. Age-Out protections and priority date retention\n##### (a) Age-Out protections\n**(1) In general**\nThe Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ) is amended\u2014\n**(A)**\nin section 101(b) ( 8 U.S.C. 1101(b) ), by adding at the end the following:\n(6) Determination of child status A determination as to whether an alien is a child shall be made as follows: (A) In general For purposes of a petition under section 204 and any subsequent application for an immigrant visa or adjustment of status, such determination shall be made using the age of the alien on the earlier of\u2014 (i) the date on which the petition is filed with the Secretary of Homeland Security; or (ii) the date on which an application for a labor certification under section 212(a)(5)(A)(i) is filed with the Secretary of Labor. (B) Certain dependents of nonimmigrants With respect to an alien who, for an aggregate period of 8 years before attaining the age of 21, was in the status of a dependent child of a nonimmigrant pursuant to a lawful admission as an alien eligible to be employed in the United States (other than a nonimmigrant described in subparagraph (A), (G), (N), or (S) of section 101(a)(15)), notwithstanding clause (i), the determination of the alien\u2019s age shall be based on the date on which such initial nonimmigrant employment-based petition or application was filed by the alien\u2019s nonimmigrant parent. (C) Failure to acquire status as alien lawfully admitted for permanent residence With respect to an alien who has not sought to acquire status as an alien lawfully admitted for permanent residence during the 2 years beginning on the date on which an immigrant visa becomes available to such alien, the alien\u2019s age shall be determined based on the alien\u2019s biological age, unless the failure to seek to acquire such status was due to extraordinary circumstances. ; and\n**(B)**\nin section 201(f) ( 8 U.S.C. 1151 )\u2014\n**(i)**\nby striking the subsection heading and all that follows through Termination Date.\u2014 in paragraph (3) and inserting Rule for Determining Whether Certain Aliens are Immediate Relatives.\u2014 ; and\n**(ii)**\nby striking paragraph (4).\n**(2) Effective date**\n**(A) In general**\nThe amendments made by this subsection shall be effective as if included in the Child Status Protection Act ( Public Law 107\u2013208 ; 116 Stat. 927).\n**(B) Motion to reopen or reconsider**\n**(i) In general**\nA motion to reopen or reconsider the denial of a petition or application described in the amendment made by paragraph (1)(A) may be granted if\u2014\n**(I)**\nsuch petition or application would have been approved if the amendment described in such paragraph had been in effect at the time of adjudication of the petition or application;\n**(II)**\nthe individual seeking relief pursuant to such motion was in the United States at the time the underlying petition or application was filed; and\n**(III)**\nsuch motion is filed with the Secretary of Homeland Security or the Attorney General not later than the date that is 2 years after the date of the enactment of this Act.\n**(ii) Exemption from numerical limitations**\nNotwithstanding any other provision of law, an individual granted relief pursuant to a motion to reopen or reconsider under clause (i) shall be exempt from the numerical limitations in sections 201, 202, and 203 of the Immigration and Nationality Act ( 8 U.S.C. 1151 , 1152, and 1153).\n##### (b) Nonimmigrant dependent children\nSection 214 of the Immigration and Nationality Act ( 8 U.S.C. 1184 ) is amended by adding at the end the following:\n(s) Derivative beneficiaries (1) In general Except as described in paragraph (2), the determination as to whether an alien who is the derivative beneficiary of a properly filed pending or approved immigrant petition under section 204 is eligible to be a dependent child shall be based on whether the alien is determined to be a child under section 101(b)(6). (2) Long-term dependents If otherwise eligible, an alien who is determined to be a child pursuant to section 101(b)(6)(B) may change status to, or extend status as, a dependent child of a nonimmigrant with an approved employment-based petition under this section or an approved application under section 101(a)(15)(E), notwithstanding such alien\u2019s marital status. (3) Employment authorization An alien admitted to the United States as a dependent child of a nonimmigrant who is described in this section is authorized to engage in employment in the United States incident to status. .\n##### (c) Priority date retention\nSection 203(h) of the Immigration and Nationality Act ( 8 U.S.C. 1153(h) ) is amended\u2014\n**(1)**\nby striking the subsection heading and inserting Retention of Priority Dates ;\n**(2)**\nby striking paragraphs (1) through (4);\n**(3)**\nby redesignating paragraph (5) as paragraph (3); and\n**(4)**\nby inserting before paragraph (3) the following:\n(1) In general The priority date for an individual shall be the date on which a petition under section 204 is filed with the Secretary of Homeland Security or the Secretary of State, as applicable, unless such petition was preceded by the filing of a labor certification with the Secretary of Labor, in which case the date on which the labor certification is files shall be the priority date. (2) Applicability The principal beneficiary and all derivative beneficiaries shall retain the priority date associated with the earliest of any approved petition or labor certification, and such priority date shall be applicable to any subsequently approved petition. .",
      "versionDate": "2025-09-18",
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
        "actionDate": "2025-09-19",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "5528",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "America\u2019s CHILDREN Act of 2025",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-07-15",
        "text": "Referred to the Committee on the Judiciary, and in addition to the Committees on Homeland Security, Ways and Means, Transportation and Infrastructure, Education and Workforce, Oversight and Government Reform, and Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4393",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "DIGNIDAD (Dignity) Act of 2025",
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
        "name": "Immigration",
        "updateDate": "2025-11-18T18:31:06Z"
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
      "date": "2025-09-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2886is.xml"
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
      "title": "America\u2019s CHILDREN Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-04T12:03:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protecting Children of Long-Term Visa Holders Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-10T06:08:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "America\u2019s CHILDREN Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-10T06:08:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Immigration and Nationality Act to authorize lawful permanent resident status for certain college graduates who entered the United States as children, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-10T06:03:27Z"
    }
  ]
}
```
