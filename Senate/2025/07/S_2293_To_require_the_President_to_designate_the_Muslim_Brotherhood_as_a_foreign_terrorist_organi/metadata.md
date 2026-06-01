# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2293?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2293
- Title: Muslim Brotherhood Terrorist Designation Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2293
- Origin chamber: Senate
- Introduced date: 2025-07-15
- Update date: 2026-04-23T11:03:25Z
- Update date including text: 2026-04-23T11:03:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-15: Introduced in Senate
- 2025-07-15 - IntroReferral: Introduced in Senate
- 2025-07-15 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2025-07-15: Introduced in Senate

## Actions

- 2025-07-15 - IntroReferral: Introduced in Senate
- 2025-07-15 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-15",
    "latestAction": {
      "actionDate": "2025-07-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2293",
    "number": "2293",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "C001098",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Cruz, Ted [R-TX]",
        "lastName": "Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Muslim Brotherhood Terrorist Designation Act of 2025",
    "type": "S",
    "updateDate": "2026-04-23T11:03:25Z",
    "updateDateIncludingText": "2026-04-23T11:03:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-15",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-15",
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
            "date": "2025-07-15T22:20:11Z",
            "name": "Referred To"
          },
          {
            "date": "2025-07-15T22:20:11Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "AR"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "FL"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "FL"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "PA"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "AR"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "IA"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "TX"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-07-22",
      "state": "TN"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-07-28",
      "state": "NC"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "PA"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2026-04-22",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2293is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2293\nIN THE SENATE OF THE UNITED STATES\nJuly 15, 2025 Mr. Cruz (for himself, Mr. Cotton , Mrs. Moody , Mr. Scott of Florida , Mr. McCormick , and Mr. Boozman ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo require the President to designate the Muslim Brotherhood as a foreign terrorist organization, to direct the Secretary of State to submit a report to Congress regarding such designation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Muslim Brotherhood Terrorist Designation Act of 2025 .\n#### 2. Prohibitions on Muslim Brotherhood operations in the United States\n##### (a) Findings; determinations\nSection 1002 of the Anti-Terrorism Act of 1987 ( 22 U.S.C. 5201 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (6), by striking and at the end;\n**(B)**\nin paragraph (7), by striking the period at the end and inserting a semicolon; and\n**(C)**\nby adding at the end the following:\n(8) Hamas is a Muslim Brotherhood branch, according to its charter, which describes Hamas as one of the wings of the Muslim Brotherhood in Palestine ; (9) the Counter Terrorism Guide, published by the National Counterterrorism Center, states Hamas\u2019s roots are in the Palestinian branch of the Muslim Brotherhood ; (10) Hamas has been designated as a foreign terrorist organization by the Secretary of State pursuant to section 219(a) of the Immigration and Nationality Act ( 8 U.S.C. 1189(a) ) and as a Specially Designated Global Terrorist pursuant to Executive Order 13224 ( 50 U.S.C. 1701 note; relating to blocking property and prohibiting transactions with persons who commit, threaten to commit, or support terrorism); (11) on October 7, 2023, Hamas terrorists committed the worst 1-day massacre of Jews since the Holocaust, which included the murder, kidnapping, or disappearance of at least 53 United States citizens; (12) the Muslim Brotherhood functions as a global organization and provides material support to Muslim Brotherhood branches in countries and territories by providing political support, financial resources, training, services, expert advice, and communications assistance; and (13) Muslim Brotherhood branches have sought to destabilize and undermine United States allies and partners throughout the Middle East, including in Bahrain, Egypt, Jordan, Saudi Arabia, and the United Arab Emirates, and have been outlawed as a terrorist group by the governments of those countries. ; and\n**(2)**\nin subsection (b), by striking the PLO and its affiliates are a terrorist organization and and replacing with the PLO, the Muslim Brotherhood, and their affiliates are terrorist organizations and are .\n##### (b) Prohibitions\nSection 1003 of the Anti-Terrorism Act of 1987 ( 22 U.S.C. 5202 ) is amended\u2014\n**(1)**\nin the section title, by striking PLO and inserting the PLO and the Muslim Brotherhood ;\n**(2)**\nin the matter preceding paragraph (1), by striking or any of its and inserting , the Muslim Brotherhood, or any of their respective ; and\n**(3)**\nby striking or any of its each place such phrase appears and inserting , the Muslim Brotherhood, or any of their .\n##### (c) Termination\nSection 1005(b) of the Anti-Terrorism Act of 1987 ( 22 U.S.C. 5201 note) is amended by inserting , with respect to prohibitions regarding the PLO, after this title .\n##### (d) Immigration restrictions\nThe Anti-Terrorism Act of 1987 ( 22 U.S.C. 5201 et seq. ) is amended by adding at the end the following:\n1006. Mandatory ineligibility for visas, admission, or parole for Muslim Brotherhood members The Secretary of State shall impose the sanctions authorized under section 306(b)(1) of the Robert Levinson Hostage Recovery and Hostage-Taking Accountability Act ( 22 U.S.C. 1741d(b)(1) ) with respect to any foreign person the President determines, based on credible evidence, is a Muslim Brotherhood member, including the measures\u2014 (1) related to inadmissibility and ineligibility described in subparagraph (A) of such section; and (2) requiring the immediate revocation of current visas in accordance with subparagraph (B) of such section. 1007. Definitions In this title: (1) Foreign person The term foreign person means an individual or entity that is not a United States person. (2) Muslim brotherhood The term Muslim Brotherhood means the Society of the Muslim Brothers (also known as Jama'at al-Ikhwan al-Muslimin ). (3) Muslim brotherhood branch The term Muslim Brotherhood branch means any entity that is a branch, charity, or organization that is directly or indirectly owned or controlled, or otherwise directly or indirectly affiliated with the Muslim Brotherhood including\u2014 (A) Hamas and Lajnat al-Daawa al-Islamiya; and (B) any other such organization operating in Algeria, Bahrain, Bangladesh, Belgium, Canada, Egypt, France, Gaza, Germany, India, Indonesia, Iran, Iraq, Jordan, Judea and Samaria, Kuwait, Lebanon, Libya, Malaysia, Mauritania, Morocco, Oman, Pakistan, Qatar, Saudi Arabia, Somalia, South Africa, Sudan, Syria, Tunisia, Turkey, United Arab Emirates, United Kingdom, Yemen, or in any other country or jurisdiction identified by the Secretary of State. (4) Muslim brotherhood member The term Muslim Brotherhood member means an individual who is a member of, under the control of, or serving as a representative of, the Muslim Brotherhood or a Muslim Brotherhood branch. (5) United States person The term United States person means\u2014 (A) a United States citizen; (B) a permanent resident of the United States; (C) a foreign national who is residing in the United States; and (D) an entity organized under the laws of the United States or of any jurisdiction of the United States, including a foreign branch of such an entity. .\n#### 3. Designation of Muslim Brotherhood entities as foreign terrorist organizations\n##### (a) Definitions\nIn this section:\n**(1) Muslim brotherhood; muslim brotherhood branch; muslim brotherhood member**\nThe terms Muslim Brotherhood , Muslim Brotherhood branch , and Muslim Brotherhood member have the meanings given such terms in section 1007 of the Anti-Terrorism Act of 1987, as added by section 2(d).\n**(2) Relevant congressional committees**\nThe term relevant congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Relations of the Senate ; and\n**(B)**\nthe Committee on Foreign Affairs of the House of Representatives .\n##### (b) Annual report\nNot later than 90 days after the date of the enactment of this Act, and annually thereafter, the Secretary of State shall submit a report to the relevant congressional committees that\u2014\n**(1)**\nidentifies all Muslim Brotherhood branches, including branches operating in the countries and jurisdictions described in section 1007(2)(B) of the Anti-Terrorism Act of 1987, as added by section 2(d); and\n**(2)**\nfor each such Muslim Brotherhood branch, includes a determination of whether\u2014\n**(A)**\nthe Muslim Brotherhood branch has been designated pursuant to any of the authorities described in subsection (c); and\n**(B)**\nthe activities of such Muslim Brotherhood branch meets the criteria for such designation, or whether such entities engaged in conduct that may be constitute a ground for such designation, pursuant to any of the authorities described in subsection (c).\n##### (c) Authorities described\nThe authorities described in this subsection are the laws authorizing the designation of an entity as\u2014\n**(1)**\na foreign terrorist organization under section 219(a) of the Immigration and Nationality Act ( 8 U.S.C. 1189(a) ); or\n**(2)**\na Specially Designated Global Terrorist pursuant to Executive Order 13224 ( 50 U.S.C. 1701 note; relating to blocking property and prohibiting transactions with persons who commit, threaten to commit, or support terrorism).\n##### (d) Sanctions\n**(1) In general**\nNot later than 90 days after the date of the enactment of this Act, the President shall impose the sanctions described in paragraph (3) with respect to the Muslim Brotherhood or any successor organization.\n**(2) Sanctions against muslim brotherhood branches**\n**(A) In general**\nNot later than 30 days after the submission of each report pursuant to subsection (b), in the case of any positive determination made related to a Muslim Brotherhood branch the President shall impose\u2014\n**(i)**\nthe sanctions described in paragraph (3)(A) on any Muslim Brotherhood branch that has been designated pursuant to subsection (c)(2)(A); and\n**(ii)**\nthe sanctions described in paragraph (3)(B) on any Muslim Brotherhood branch whose activities meet the criteria for such designation in accordance with subsection (b)(2)(B).\n**(B) Minimum period**\nThe President may not remove the sanctions described in paragraph (3) from the Muslim Brotherhood during the 4-year period beginning on the date of the report in which such positive determination regarding a Muslim Brotherhood branch was made.\n**(3) Sanctions described**\nThe sanctions described in this paragraph are\u2014\n**(A)**\ndesignation as a foreign terrorist organization pursuant to section 219(a) of the Immigration and Nationality Act ( 8 U.S.C. 1189(a) ); and\n**(B)**\nimposition of the sanctions applicable with respect to a foreign person pursuant to Executive Order 13224 ( 50 U.S.C. 1701 note; relating to blocking property and prohibiting transactions with persons who commit, threaten to commit, or support terrorism).\n##### (e) Form\nThe report required under subsection (b) shall be submitted in unclassified form, but may include a classified annex, if appropriate.",
      "versionDate": "2025-07-15",
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
        "actionDate": "2025-07-15",
        "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4397",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Muslim Brotherhood Terrorist Designation Act of 2025",
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
        "name": "International Affairs",
        "updateDate": "2025-07-31T19:56:38Z"
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
      "date": "2025-07-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2293is.xml"
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
      "title": "Muslim Brotherhood Terrorist Designation Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-23T11:03:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Muslim Brotherhood Terrorist Designation Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-31T04:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the President to designate the Muslim Brotherhood as a foreign terrorist organization, to direct the Secretary of State to submit a report to Congress regarding such designation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-31T04:18:25Z"
    }
  ]
}
```
