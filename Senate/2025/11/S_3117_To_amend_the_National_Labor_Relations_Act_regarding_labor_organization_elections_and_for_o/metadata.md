# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3117?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3117
- Title: Worker RESULTS Act
- Congress: 119
- Bill type: S
- Bill number: 3117
- Origin chamber: Senate
- Introduced date: 2025-11-06
- Update date: 2025-11-19T15:39:39Z
- Update date including text: 2025-11-19T15:39:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-06: Introduced in Senate
- 2025-11-06 - IntroReferral: Introduced in Senate
- 2025-11-06 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-11-06: Introduced in Senate

## Actions

- 2025-11-06 - IntroReferral: Introduced in Senate
- 2025-11-06 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-06",
    "latestAction": {
      "actionDate": "2025-11-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3117",
    "number": "3117",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
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
    "title": "Worker RESULTS Act",
    "type": "S",
    "updateDate": "2025-11-19T15:39:39Z",
    "updateDateIncludingText": "2025-11-19T15:39:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-06",
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
      "actionDate": "2025-11-06",
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
          "date": "2025-11-06T16:19:00Z",
          "name": "Referred To"
        }
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
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-11-06",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3117is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3117\nIN THE SENATE OF THE UNITED STATES\nNovember 6, 2025 Mr. Cassidy (for himself and Mr. Tuberville ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the National Labor Relations Act regarding labor organization elections, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Worker Reforming Elections for Speedy and Unimpeded Labor Talks Act or the Worker RESULTS Act .\n#### 2. Amendments to the National Labor Relations Act regarding elections\n##### (a) Certification bar; extension of recertification window; decertification during initial bargaining phase\n**(1) In general**\nSection 9(c)(3) of the National Labor Relations Act ( 29 U.S.C. 159(c)(3) ) is amended\u2014\n**(A)**\nby striking No election and inserting (A) No election ;\n**(B)**\nby striking held. and inserting the following: \u201cheld in which a majority of the employees in the bargaining unit fail to select a representative for purposes of collective bargaining.\n(B) (i) In the case of a valid election in which the majority of the employees in a bargaining unit select a representative for purposes of collective bargaining, the Board shall dismiss any petition for an election under this subsection with respect to the bargaining unit, or any subdivision, that is filed before there is collective bargaining agreement with respect to the employees in effect between the representative and the employer of the employees. (ii) (I) If the Board determines that, during the initial collective bargaining phase for an employer and a representative selected for purposes of collective bargaining by the employees of the bargaining unit, the representative is not bargaining collectively in good faith with the employer, then\u2014 (aa) there shall be a 90-day period, beginning on the date that is 60 days after the Board makes such determination and ending on the date that is 150 days after such determination (referred to in this clause as the decertification window period ), during which a petition may be filed in accordance with paragraph (1)(A)(ii) or subsection (e)(1), as applicable; and (bb) not later than 45 days before the first day of the decertification window period, the Board shall provide notice to each employee in the bargaining unit regarding the Board's determination under this clause. (II) In this clause, the term initial collective bargaining phase means the period beginning on the date of a valid election in which the majority of employees in a bargaining unit select a representative for purposes of collective bargaining and ending on the day before the date on which such representative and the employer of the employees enter into the initial collective bargaining agreement. (C) With respect to an employer and a representative of employees of the employer in a bargaining unit, beginning on the date on which the first collective bargaining agreement takes effect between such employer and such representative with respect to such unit, the Board shall dismiss any petition for an election under this subsection with respect to the bargaining unit unless the petition is filed\u2014 (i) during any period during which a collective bargaining agreement between the employer and such representative with respect to such unit is not in effect; or (ii) during any window period applicable to the employer and representative with respect to such unit, in accordance with subparagraph (D). (D) (i) For purposes of subparagraph (C) and subject to clause (ii), the term window period , with respect to an employer and a representative of employees of the employer in a bargaining unit, means a 90-day period beginning 150 days and ending 60 days before\u2014 (I) the last day of the 2-year period beginning on the date on which the first collective bargaining agreement between the employer and representative of such employees took effect; or (II) the last day of each consecutive 2-year period thereafter. (ii) In the case of an employer that is a health care institution, clause (i) shall be applied by substituting 180 days for 150 days and by substituting 90 days for 60 days . ;\n**(C)**\nby striking Employees and inserting the following:\n(E) Employees ; and\n**(D)**\nby striking In any election and inserting the following:\n(F) In any election .\n**(2) Clarification**\nSection 8 of the National Labor Relations Act ( 29 U.S.C. 158 ) is amended by adding at the end the following:\n(h) It shall not be an unfair labor practice under subsection (a) or (b) for any person to inform employees of their rights under subparagraph (B)(ii) or (C) of section 9(c)(3). .\n##### (b) Requirement for secret ballot elections\nSection 9(a) of the National Labor Relations Act ( 29 U.S.C. 159(a) ) is amended by striking designated or selected for the purposes of collective bargaining and inserting for the purposes of collective bargaining selected by secret ballot, in an election conducted by the Board, .\n##### (c) Quorum\nSection 9 of the National Labor Relations Act ( 29 U.S.C. 159 ), as amended by this section, is further amended\u2014\n**(1)**\nin subsection (a), by inserting That, in certifying a representative as the exclusive representative of all employees in a unit for such purposes of collective bargaining, the majority shall be the majority of voters in a secret ballot election in which not less than two-thirds of all employees in the unit vote: Provided further , after employment: Provided , ; and\n**(2)**\nin subsection (c)(3)(F), as designated by subsection (a), by inserting of the votes, when not less than two-thirds of all employees in the unit vote, after majority .\n##### (d) Removal of settlement bar\nSection 9(c) of the National Labor Relations Act ( 29 U.S.C. 159(c) ) is amended by adding at the end the following:\n(6) The Board shall not prohibit or postpone, or impose any bar or delay on, any recognition election based on a petition by a party due to a settlement of any unfair labor practice charge against either party. .\n##### (e) Limit on Board authority\nSection 9(c) of the National Labor Relations Act ( 29 U.S.C. 159(c) ) is further amended by adding at the end the following:\n(7) The Board shall not dismiss or impose any bar or restriction regarding when an election under this section may be requested or directed, except as established in this subsection or subsections (d), (e)(2), (f), and (g). .\n##### (f) Blocking charges and no merit-Based dismissals\nSection 9 of the National Labor Relations Act ( 29 U.S.C. 159 ) is amended by adding at the end the following:\n(f) (1) Whenever any party to a representation proceeding under this section files a charge of an unfair labor practice together with a request that the charge block the process of an election under this section, or whenever any party to a representation proceeding requests that its previously filed charge of an unfair labor practice block such process, the party shall simultaneously file, but not serve on any other party, a written offer of proof in support of the charge. The offer of proof shall provide the names of the witnesses who will testify in support of the charge and a summary of each witness's anticipated testimony. The party seeking to block the process of an election under this section shall also promptly make available to the regional director the witnesses identified in its offer of proof. (2) Except as provided in paragraph (3), the ballots for an election in a case described in paragraph (1) shall be promptly opened and counted at the conclusion of the election. (3) If the charge in a case described in paragraph (1) is filed that alleges a violation of subsection (a)(1), (a)(2), or (b)(1)(A) of section 8 and that challenges the circumstances surrounding the petition for the election or the showing of interest submitted in support of such petition, or if a charge is filed in a case described in paragraph (1) that alleges an employer has dominated a labor organization in violation of section 8(a)(2) and that seeks to disestablish a bargaining relationship, the regional director shall impound the ballots for the election for a period not to exceed 60 days from the conclusion of the election unless the charge has been withdrawn or dismissed prior to the conclusion of the election. If a complaint issues with respect to such charge at any time prior to the expiration of that period of not more than 60 days, the ballots for the election shall continue to be impounded until there is a final determination regarding the charge and its effect, if any, on the election petition. If the charge is withdrawn or dismissed at any time during that period, or if the period ends without a complaint issuing, the ballots shall be promptly opened and counted. The period of not more than 60 days under this paragraph shall not be extended, even if more than one charge of an unfair labor practice is filed serially. (4) In any case described in paragraph (1), the certification of results (including, where appropriate, a certification of representative) for the election shall not issue until there is a final disposition of the charge and a determination of its effect, if any, on the election petition. (g) In any case in which there is a representation proceeding involving an employer and also a charge of an unfair labor practice against any party to the representation proceeding, a regional director shall dismiss the representation proceeding due to an unfair labor practice charge only if such charge is found to be meritorious through a formal evidentiary hearing. .\n##### (g) No successor bar\nSection 9 of the National Labor Relations Act ( 29 U.S.C. 159 ), as amended by this section, is further amended by adding at the end the following:\n(h) With respect to any successor employer (defined, for purposes of this subsection, as an employer who acquires substantially all of the property used in a trade or business of another employer), the Board shall not prohibit or postpone, or impose any bar or delay on the timing of, the filing of a petition for an election under this section based on the acquisition by the successor employer. .\n##### (h) Unfair labor practice To enter into no-Raid agreements\n**(1) In general**\nSection 8(b) of the National Labor Relations Act ( 29 U.S.C. 158(b) ) is amended\u2014\n**(A)**\nin paragraph (6), by striking and after the semicolon;\n**(B)**\nby redesignating paragraph (7) as paragraph (8);\n**(C)**\nby inserting after paragraph (6) the following:\n(7) to enter into an agreement with any other labor organization, or its agents, in which a labor organization agrees to not solicit, compete for, organize for purposes of collective bargaining, or otherwise represent, a group of employees of an employer, or of a certain trade, class, or craft; and ; and\n**(D)**\nin the matter following paragraph (8), as so redesignated, by striking this paragraph (7) and inserting this paragraph (8) .\n**(2) Conforming amendments**\nSection 10(l) of the National Labor Relations Act ( 29 U.S.C. 160(l) ) is amended by striking section 8(b)(7) each place the term appears and inserting section 8(b)(8) .",
      "versionDate": "2025-11-06",
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
        "name": "Labor and Employment",
        "updateDate": "2025-11-19T15:39:39Z"
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
      "date": "2025-11-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3117is.xml"
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
      "title": "Worker RESULTS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-08T05:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Worker RESULTS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-08T05:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Worker Reforming Elections for Speedy and Unimpeded Labor Talks Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-08T05:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the National Labor Relations Act regarding labor organization elections, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-08T05:33:23Z"
    }
  ]
}
```
