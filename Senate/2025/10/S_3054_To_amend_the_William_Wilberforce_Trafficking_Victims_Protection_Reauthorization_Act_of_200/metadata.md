# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3054?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3054
- Title: Kayla Hamilton Act
- Congress: 119
- Bill type: S
- Bill number: 3054
- Origin chamber: Senate
- Introduced date: 2025-10-23
- Update date: 2026-03-27T14:30:49Z
- Update date including text: 2026-03-27T14:30:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-10-23: Introduced in Senate
- 2025-10-23 - IntroReferral: Introduced in Senate
- 2025-10-23 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-10-23: Introduced in Senate

## Actions

- 2025-10-23 - IntroReferral: Introduced in Senate
- 2025-10-23 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-23",
    "latestAction": {
      "actionDate": "2025-10-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3054",
    "number": "3054",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
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
    "title": "Kayla Hamilton Act",
    "type": "S",
    "updateDate": "2026-03-27T14:30:49Z",
    "updateDateIncludingText": "2026-03-27T14:30:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-23",
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
      "actionDate": "2025-10-23",
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
            "date": "2025-10-23T20:08:19Z",
            "name": "Referred To"
          },
          {
            "date": "2025-10-23T20:08:19Z",
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
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-10-23",
      "state": "TX"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2025-10-23",
      "state": "SC"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-10-23",
      "state": "TN"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-10-23",
      "state": "NC"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-10-23",
      "state": "WY"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-10-23",
      "state": "LA"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-10-23",
      "state": "NC"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-10-23",
      "state": "AL"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-10-23",
      "state": "MO"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-10-23",
      "state": "AL"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-10-27",
      "state": "LA"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "ID"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3054is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3054\nIN THE SENATE OF THE UNITED STATES\nOctober 23, 2025 Mr. Cornyn (for himself, Mr. Cruz , Mr. Graham , Mrs. Blackburn , Mr. Tillis , Ms. Lummis , Mr. Cassidy , Mr. Budd , Mr. Tuberville , Mr. Schmitt , and Mrs. Britt ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the William Wilberforce Trafficking Victims Protection Reauthorization Act of 2008 and the Homeland Security Act of 2002 to enhance efforts to combat the trafficking of children.\n#### 1. Short title\nThis Act may be cited as the Kayla Hamilton Act .\n#### 2. Placement determinations for unaccompanied alien children\nSection 462(b)(2) of the Homeland Security Act of 2002 ( 6 U.S.C. 279(b)(2) ) is amended to read as follows:\n(2) Placement determinations for unaccompanied alien children The Director of the Office of Refugee Resettlement shall make determinations under paragraph (1)(C) in accordance with section 235(c)(2) of the William Wilberforce Trafficking Victims Protection Reauthorization Act of 2008 ( 8 U.S.C. 1232(c)(2) ). .\n#### 3. Enhancing efforts to combat the trafficking of children\nSection 235(c) of the William Wilberforce Trafficking Victims Protection Reauthorization Act of 2008 ( 8 U.S.C. 1232(c) ) is amended\u2014\n**(1)**\nin paragraph (2), to read as follows:\n(2) Safe and secure placements (A) Initial actions The Secretary of Health and Human Services may not make a placement determination under this paragraph for an unaccompanied alien child who is in Federal custody by reason of the immigration status of that child until the Secretary does the following: (i) Consultations The Secretary of Health and Human Services shall consult with the Secretary of Homeland Security and the Attorney General (including appropriate juvenile justice officials)\u2014 (I) to ensure that the unaccompanied alien child will appear for all immigration, administrative, and judicial hearings or proceedings in which the child is involved; (II) to ensure that the unaccompanied alien child will be protected from smugglers, traffickers, gangs, and others who might seek to victimize or otherwise engage the child in criminal, harmful, or exploitative activity; and (III) to determine if the unaccompanied alien child\u2014 (aa) is a flight risk; (bb) is a danger to self, another individual, or the community; or (cc) has been arrested for, charged with, or convicted of any criminal offense in the United States or in his or her country of citizenship, nationality, or last habitual residence. (ii) Screening for gang related activity; requirement to obtain criminal records In the case of an unaccompanied alien child 12 years of age or older, the Secretary of Health and Human Services shall\u2014 (I) contact the consulate or embassy of the country of citizenship, nationality, or last habitual residence for the unaccompanied alien child to obtain any relevant arrest records, pending criminal charges, or conviction documents involving such child; and (II) conduct an examination of the unaccompanied alien child to determine if such child has any gang-related tattoos and other gang-related markings. (B) Placement generally (i) In general Except as otherwise provided in this paragraph, an unaccompanied alien child who is in the custody of the Department of Health and Human Services shall be promptly placed in the least restrictive setting that is in the best interest of the child. (ii) Prohibition on release on own recognizance An unaccompanied alien child may not be released on his or her own recognizance. (C) Placement of certain unaccompanied alien children in secure facilities In the case of an unaccompanied alien child 12 years of age or older, the unaccompanied alien child shall be placed in a secure facility for the duration of any immigration proceedings (and, if ordered removed, until such unaccompanied alien child is removed) if the unaccompanied alien child\u2014 (i) is a flight risk; or (ii) is a danger to self, other individuals, or the community, including if the unaccompanied alien child\u2014 (I) has a gang-related tattoo or any other gang-related marking; (II) has been convicted of a serious criminal offense (as defined in section 101(h) of the Immigration and Nationality Act ( 8 U.S.C. 1101(h) )) in any State or territory of the United States or in the unaccompanied alien child\u2019s country of citizenship, nationality, or last habitual residence; (III) has been convicted of any aggravated felony (as defined in section 101(a)(43) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(43) )); or (IV) has, for conduct in connection with gang affiliation or gang activity in any State or territory of the United States or in the unaccompanied alien child\u2019s country of citizenship, nationality, or last habitual residence\u2014 (aa) any arrest record; (bb) any pending criminal charge; (cc) any other pending proceeding; or (dd) any conviction. (D) Prohibitions on placement of unaccompanied alien children with certain individuals The Secretary of Health and Human Services shall not place an unaccompanied alien child in the custody of any individual who is one or more of the following: (i) Secure and stable sponsors An individual who is not a United States citizen or a lawful permanent resident of the United States. (ii) Individuals with criminal history An individual who has been convicted of, or who resides in a household with an individual who has been convicted of\u2014 (I) a sex offense (as defined in section 111(5) of the Sex Offender Registration and Notification Act ( 34 U.S.C. 20911(5) )); (II) a crime involving severe forms of trafficking in persons (as defined in section 103(11) of the Trafficking Victims Protection Act of 2000 ( 22 U.S.C. 7102(11) )); (III) a crime of domestic violence (as defined in section 40002(a)(12) of the Violence Against Women Act of 1994 ( 34 U.S.C. 12291(a)(12) )); (IV) a crime of child abuse and neglect (as defined in section 3 of the Child Abuse Prevention and Treatment Act ( Public Law 93\u2013247 ; 42 U.S.C. 5101 note)); (V) murder, manslaughter, or an attempt to commit murder or manslaughter (as defined in sections 1111, 1112, and 1113 of title 18, United States Code); (VI) a crime involving the receipt, distribution, or possession of a visual depiction of a minor engaging in sexually explicit conduct (as described in section 2252 of title 18, United States Code); (VII) any crime for which an alien is required to be taken into custody pursuant to section 236(c)(1) of the Immigration and Nationality Act ( 8 U.S.C. 1226(c)(1) ); (VIII) any aggravated felony (as defined in section 101 of the Immigration and Nationality Act); (IX) any crime defined as a felony by the relevant jurisdiction (Federal, State, tribal, or local); (X) any crime punishable by more than 1 year of imprisonment; or (XI) any other criminal offense as designated by the Attorney General, in the Attorney General\u2019s sole and unreviewable discretion. ; and\n**(2)**\nin paragraph (3)\u2014\n**(A)**\nin subparagraph (A), by striking Subject to the requirements of subparagraph (B) and inserting Subject to the requirements of subparagraphs (B) and (D) ; and\n**(B)**\nby inserting at the end the following:\n(D) Information about individuals with whom children are placed Before placing a child with any individual, the Secretary of Health and Human Services shall provide to the Secretary of Homeland Security, with regard to the individual with whom the child will be placed and each adult resident of the individual\u2019s household, information on\u2014 (i) the name of the individual and each adult resident of the individual\u2019s household; (ii) the social security number or individual taxpayer identification number of the individual and each adult resident of the individual\u2019s household; (iii) the date of birth of the individual and of each adult resident of the individual\u2019s household; (iv) the physical location and address of the individual\u2019s residence where the child will be placed; (v) the immigration status of the individual and each adult resident of the individual\u2019s household; (vi) contact information for the individual and for each adult resident of the individual\u2019s household, including telephone numbers, email addresses, and work telephone numbers (if available); and (vii) the results of all background and criminal records checks conducted on the individual and each adult resident of the individual\u2019s household, which shall include at a minimum an investigation of the Dru Sjodin National Sex Offender Public Website, a public records background check, and a national criminal history background check based on fingerprints. .\n#### 4. Construction; severability\nAny provision of the this Act or an amendment made by this Act held to be invalid or unenforceable by its terms, or as applied to any person or circumstance, shall be construed so as to give it the maximum effect permitted by law, unless such holding shall be utterly invalid or unenforceable, in which event such provision shall be deemed severable from this Act and shall not affect the remainder of this Act, or the application of such provision to other persons not similarly situated or to other, dissimilar circumstances.\n#### 5. Exemption from Paperwork Reduction Act and the Administrative Procedure Act\n##### (a) Paperwork reduction act\nNothing in this Act may be construed to require the Secretary of Homeland Security, the Secretary of Health and Human Services, the Secretary of State, or the Attorney General to comply with the requirements of chapter 35 of title 44, United States Code (commonly referred to as the Paperwork Reduction Act ) if such individuals determine that compliance would impede the immediate implementation of this Act or the amendments made by this Act.\n##### (b) Administrative procedure act\nNothing in this Act may be construed to require the Secretary of Homeland Security, the Secretary of Health and Human Services, the Secretary of State, or the Attorney General to promulgate regulations under subchapter II of chapter 5 of title 5, United States Code (commonly referred to as the Administrative Procedure Act ), if such individuals determine that compliance would impede the immediate implementation of this Act or the amendments made by this Act.\n#### 6. Effective date; applicability\n##### (a) In general\nExcept as provided in subsection (b), this Act and the amendments made by this shall take effect on the date of the enactment of this Act.\n##### (b) Applicability\nThis Act and the amendments made by this Act shall apply to any release and custody determinations for an unaccompanied alien child (as defined in section 642(g)(2) of the Homeland Security Act of 2002), that are pending or occur on or after the date of the enactment of this Act, and all release redeterminations.",
      "versionDate": "2025-10-23",
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
        "actionDate": "2025-12-17",
        "text": "Received in the Senate."
      },
      "number": "4371",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Kayla Hamilton Act",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-12-03T18:31:48Z"
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
      "date": "2025-10-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3054is.xml"
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
      "title": "Kayla Hamilton Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-11T12:03:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Kayla Hamilton Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-29T06:08:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the William Wilberforce Trafficking Victims Protection Reauthorization Act of 2008 and the Homeland Security Act of 2002 to enhance efforts to combat the trafficking of children.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-29T06:03:22Z"
    }
  ]
}
```
