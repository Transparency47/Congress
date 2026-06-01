# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4224?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4224
- Title: Dalilah’s Law Act
- Congress: 119
- Bill type: S
- Bill number: 4224
- Origin chamber: Senate
- Introduced date: 2026-03-26
- Update date: 2026-04-13T17:55:00Z
- Update date including text: 2026-04-13T17:55:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-26: Introduced in Senate
- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-03-26: Introduced in Senate

## Actions

- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-26",
    "latestAction": {
      "actionDate": "2026-03-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4224",
    "number": "4224",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Dalilah\u2019s Law Act",
    "type": "S",
    "updateDate": "2026-04-13T17:55:00Z",
    "updateDateIncludingText": "2026-04-13T17:55:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-26",
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
      "actionDate": "2026-03-26",
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
          "date": "2026-03-26T17:34:48Z",
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
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "NC"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "WV"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "WY"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4224is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4224\nIN THE SENATE OF THE UNITED STATES\nMarch 26, 2026 Mr. Cornyn (for himself, Mr. Budd , Mrs. Capito , Ms. Lummis , and Mr. Tuberville ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to prohibit certain aliens from presenting or using a commercial driver\u2019s license in interstate or foreign commerce, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Dalilah\u2019s Law Act .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nTITLE I\u2014Keeping our roads safe\nSec. 101. Use of commercial driver\u2019s licenses by illegal aliens in interstate commerce.\nSec. 102. Death penalty aggravating factor.\nSec. 103. Immigration consequences.\nTITLE II\u2014Transportation\nSec. 201. Commercial driver\u2019s licenses.\nI\nKeeping our roads safe\n#### 101. Use of commercial driver\u2019s licenses by illegal aliens in interstate commerce\n##### (a) In general\nChapter 2 of title 18, United States Code, is amended by inserting after section 40A the following:\n40B. Use of commercial driver\u2019s licenses by illegal aliens in interstate commerce (a) Definitions In this section\u2014 (1) the terms commercial driver\u2019s license and commercial vehicle have the meanings given such terms in section 31301 of title 49; and (2) the term covered alien means an alien (as defined in section 101 of the Immigration and Nationality Act ( 8 U.S.C. 1101 )) who\u2014 (A) is described under\u2014 (i) section 237(a)(1)(C)(i) of the Immigration and Nationality Act ( 8 U.S.C. 1227(a)(1)(C)(i) ); (ii) section 212(a)(6)(A)(i) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a)(6)(A)(i) ); or (iii) section 236(c)(1) of the Immigration and Nationality Act ( 8 U.S.C. 1226(c)(1) ); or (B) has been paroled into the United States under section 212(d)(5) of the Immigration and Nationality Act ( 8 U.S.C. 1182(d)(5) ). (b) Prohibition It shall be unlawful for a covered alien to present or use a commercial driver\u2019s license in interstate or foreign commerce. (c) Criminal penalties (1) In general Subject to paragraph (2)(C), a covered alien who violates subsection (b) shall be fined under this title, imprisoned for not more than 5 years, or both. (2) Mandatory minimum sentence Except to the extent that a greater minimum sentence is otherwise provided by any other provision of law\u2014 (A) a covered alien who, while violating subsection (b), causes a motor vehicle accident while operating a commercial vehicle shall be imprisoned for not less than 1 year; (B) a covered alien who, while violating subsection (b), causes a motor vehicle accident while operating a commercial vehicle which results in bodily injury shall be imprisoned for not less than 2 years; and (C) a covered alien who, while violating subsection (b), causes a motor vehicle accident while operating a commercial vehicle which results in death shall be punished by death or by imprisonment for life. (d) State officials (1) In general It shall be unlawful for any officer, employee, or contractor of a State or local government, acting under color of law, to intentionally direct or implement the issuance of a commercial driver\u2019s license unless, before such issuance, the officer, employee, or contractor confirms the immigration status of the applicant through the E-Verify Program described in section 403(a) of the Illegal Immigration Reform and Immigrant Responsibility Act of 1996 ( 8 U.S.C. 1324a note; Public Law 104\u2013208 ) or an analogous State verification program. (2) Penalty An officer, employee, or contractor of a State or local government who violates paragraph (1) shall be fined under this title, imprisoned for not more than 1 year, or both. (e) Civil penalties Any business, corporation, organization, or entity that knowingly provides substantial assistance to a covered alien to violate subsection (b), or conspires with a covered alien to violate subsection (b), shall be subject to a civil penalty in an amount of $50,000 per violation. (f) Individual civil remedies (1) Action and jurisdiction Any person injured in his or her person or property in a motor vehicle accident caused by a covered alien presenting or using a commercial driver\u2019s license in interstate or foreign commerce, or his or her estate, survivors, or heirs, may bring a civil action in any appropriate district court of the United States and shall recover threefold the damages he or she sustains and the cost of the action, including attorney's fees. (2) Liability In any civil action under paragraph (1) for an injury arising from a motor vehicle accident caused by a covered alien presenting or using a commercial driver\u2019s license, liability may be asserted against any person, including any business, corporation, organization, or other entity, who aids and abets by knowingly providing substantial assistance for the covered alien to obtain, or who conspires with the covered alien to obtain, the commercial driver\u2019s license. (g) Report Not later than 180 days after the date of enactment of this section, the Attorney General shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives a written report that includes\u2014 (1) for the period beginning on such date of enactment and ending on the date of the report\u2014 (A) the total number of covered aliens arrested for violating subsection (b); (B) a State-by-State breakdown of\u2014 (i) the number of commercial driver\u2019s licenses issued to covered aliens; and (ii) the number of accidents involving covered aliens arrested for violating subsection (b); and (C) the number of arrests and prosecutions for violations of subsection (b); and (2) a plan for steps the United States Government will take to stop violations of subsection (b). .\n##### (b) Technical and conforming amendment\nThe table of sections for chapter 2 of title 18, United States Code, is amended by inserting after the item relating to section 40A the following:\n40B. Use of commercial driver\u2019s licenses by illegal aliens in interstate commerce. .\n#### 102. Death penalty aggravating factor\nSection 3592(c) of title 18, United States Code, is amended by inserting after paragraph (16) the following:\n(17) Illegal alien using a commercial driver\u2019s license and causing death in a motor vehicle crash The defendant is a covered alien (as defined in section 40B) who presents or uses a commercial driver\u2019s license (as defined in section 31301 of title 49) in interstate or foreign commerce and causes a motor vehicle accident while operating a commercial vehicle (as defined in section 31301 of title 49) which results in death. .\n#### 103. Immigration consequences\n##### (a) Aggravated felony\nSection 101(a)(43) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(43) ) is amended\u2014\n**(1)**\nin subparagraph (T), by striking and at the end;\n**(2)**\nin subparagraph (U), by striking the period at the end and inserting ; and ; and\n**(3)**\nby inserting after subparagraph (U), as amended, the following:\n(V) an offense relating to the use of a commercial driver\u2019s license in interstate commerce by a covered alien described in section 40B of title 18, United States Code. .\n##### (b) Inadmissibility\nSection 212(a)(2)(F) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a)(2)(F) ) is amended to read as follows:\n(F) Use of a commercial driver\u2019s license by a covered alien Any alien who a consular officer or the Attorney General knows, or has reason to believe, has engaged, is engaging, or seeks to enter the United States to engage, in an offense that is described in section 40B of title 18, United States Code (relating to the use of commercial driver's licenses by illegal aliens), is inadmissible. .\nII\nTransportation\n#### 201. Commercial driver\u2019s licenses\nSection 31308 of title 49, United States Code, is amended\u2014\n**(1)**\nin the matter preceding paragraph (1), in the first sentence\u2014\n**(A)**\nby inserting (referred to in this section as the Secretary ) after Secretary of Transportation ; and\n**(B)**\nby striking After and inserting the following:\n(a) Uniform standards After ;\n**(2)**\nin subsection (a) (as so designated)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin subparagraph (A), by striking and at the end;\n**(ii)**\nin subparagraph (B), by adding and after the semicolon at the end; and\n**(iii)**\nby adding at the end the following:\n(C) present written documentation to the State, obtained through an entity participating in the E-Verify Program described in section 403(a) of the Illegal Immigration Reform and Immigrant Responsibility Act of 1996 ( 8 U.S.C. 1324a note; Public Law 104\u2013208 ) or through a process established by the State, verifying the employment eligibility of the individual; ;\n**(B)**\nin paragraph (3), by striking and at the end;\n**(C)**\nin paragraph (4)(E), by striking the period at the end and inserting ; and ; and\n**(D)**\nby adding at the end the following:\n(5) on the request of the Secretary, each State shall provide to the Secretary the written documentation described in paragraph (1)(C). ; and\n**(3)**\nby adding at the end the following:\n(b) Enforcement by the Attorney General Whenever it appears to the Attorney General that a State is engaged in, or is about to engage in, any act that constitutes, or would constitute, a violation of a requirement under paragraph (1)(C) or (5) of subsection (a), the Attorney General may initiate a civil action in a district court of the United States to enjoin such violation. (c) Enforcement by attorney general of a State (1) Definitions In this subsection: (A) Harm The term harm means\u2014 (i) any bodily injury suffered by a citizen of a State; or (ii) any monetary loss greater than $100 suffered by a State or a citizen of a State. (B) Injured State The term injured State means a State alleged, or any citizen of which is alleged, to be harmed as described in paragraph (2). (2) Action for injunctive relief The attorney general of a State, or any other authorized State officer, alleging a violation of the requirement that the employment eligibility of an individual be verified through the E-Verify Program or other process described in subsection (a)(1)(C) before that individual is issued a commercial driver\u2019s license, as required under that subsection, and that the violation harms that State or any citizen of that State, shall have standing to bring an action against the Secretary on behalf of the injured State or the citizens of the injured State in an appropriate district court of the United States to obtain injunctive relief requiring the Secretary to request from the State that issued the commercial driver\u2019s license the written documentation described in subsection (a)(1)(C). .",
      "versionDate": "2026-03-26",
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
        "updateDate": "2026-04-13T17:55:00Z"
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
      "date": "2026-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4224is.xml"
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
      "title": "Dalilah\u2019s Law Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-11T03:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Dalilah\u2019s Law Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-11T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 18, United States Code, to prohibit certain aliens from presenting or using a commercial driver's license in interstate or foreign commerce, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-11T03:48:28Z"
    }
  ]
}
```
