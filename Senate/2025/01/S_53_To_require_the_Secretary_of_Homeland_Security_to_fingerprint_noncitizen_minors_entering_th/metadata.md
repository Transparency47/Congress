# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/53?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/53
- Title: PRINTS Act
- Congress: 119
- Bill type: S
- Bill number: 53
- Origin chamber: Senate
- Introduced date: 2025-01-09
- Update date: 2025-07-21T19:32:26Z
- Update date including text: 2025-07-21T19:32:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in Senate
- 2025-01-09 - IntroReferral: Introduced in Senate
- 2025-01-09 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-01-09: Introduced in Senate

## Actions

- 2025-01-09 - IntroReferral: Introduced in Senate
- 2025-01-09 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-09",
    "latestAction": {
      "actionDate": "2025-01-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/53",
    "number": "53",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "PRINTS Act",
    "type": "S",
    "updateDate": "2025-07-21T19:32:26Z",
    "updateDateIncludingText": "2025-07-21T19:32:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-09",
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
      "actionDate": "2025-01-09",
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
          "date": "2025-01-09T20:11:56Z",
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
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "LA"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "MT"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "IA"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "IA"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "ND"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "MS"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "SD"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "MT"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "FL"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "AL"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s53is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 53\nIN THE SENATE OF THE UNITED STATES\nJanuary 9, 2025 Mrs. Blackburn (for herself, Mr. Cassidy , Mr. Daines , Ms. Ernst , Mr. Grassley , Mr. Hoeven , Mrs. Hyde-Smith , Mr. Rounds , and Mr. Sheehy ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo require the Secretary of Homeland Security to fingerprint noncitizen minors entering the United States who are suspected of being victims of human trafficking, to require the Secretary to publicly disclose the number of such minors who are fingerprinted by U.S. Customs and Border Protection (CBP) officials and the number of child traffickers who are apprehended by CBP, to impose criminal penalties on noncitizen adults who use unrelated minors to gain entry into the United States, and for other purposes.\n#### 1. Short titles\nThis Act may be cited as the Preventing the Recycling of Immigrants is Necessary for Trafficking Suspension Act or the PRINTS Act .\n#### 2. Authorization of fingerprinting of noncitizen children entering the United States to reduce child trafficking\nSection 262(c) of the Immigration and Nationality Act ( 8 U.S.C. 1302(c) ) is amended to read as follows:\n(c) The Secretary of Homeland Security, working through U.S. Customs and Border Protection, in order to reduce the number of children who are trafficked into the United States, shall obtain a set of fingerprints from any alien younger than 14 years of age who is entering the United States if a U.S. Customs and Border Protection officer suspects that such child is a victim of human trafficking, in accordance with the standards established pursuant to the Trafficking Victims Protection Act of 2000 ( 34 U.S.C. 7101 et seq. ). .\n#### 3. Criminalizing recycling of minors\n##### (a) In general\nChapter 69 of title 18, United States Code, is amended by adding at the end the following:\n1430. Recycling of minors (a) In general Any person 18 years of age or older who knowingly uses, for the purpose of gaining entry into the United States, a minor to whom the individual is not a relative or guardian, shall be fined under this title, imprisoned not more than 10 years, or both. (b) Relative In this section, the term relative means an individual related by consanguinity within the second degree, as determined by common law. .\n##### (b) Clerical amendment\nThe table of sections for chapter 69 of title 18, United States Code, is amended by adding at the end the following:\n1430. Recycling of minors. .\n#### 4. Information sharing\nWith respect to any unaccompanied alien child (as defined in section 462(g) of the Homeland Security Act of 2002 ( 6 U.S.C. 279(g) )) who is transferred from the custody of the Secretary of Homeland Security to the custody of the Secretary of Health and Human Services, the Secretary of Homeland Security shall, on request, share with the Secretary of Health and Human Services the fingerprints collected under section 262(c) of the Immigration and Nationality Act, as added by section 2.\n#### 5. Reports\n##### (a) Annual report to Congress\nThe Secretary of Homeland Security shall submit an annual report to Congress that identifies the number of minors who were fingerprinted during the most recently completed fiscal year pursuant to the authority granted under section 262(c) of the Immigration and Nationality Act, as added by section 2.\n##### (b) Online publication\nThe Secretary of Homeland Security shall post, on a monthly basis on a publicly accessible U.S. Customs and Border Protection website, the number of apprehensions during the previous month involving child traffickers who falsely claimed that a child accompanying them into the United States was a close relative.",
      "versionDate": "2025-01-09",
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
        "updateDate": "2025-02-12T12:59:27Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-09",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s53",
          "measure-number": "53",
          "measure-type": "s",
          "orig-publish-date": "2025-01-09",
          "originChamber": "SENATE",
          "update-date": "2025-03-12"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s53v00",
            "update-date": "2025-03-12"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Preventing the Recycling of Immigrants is Necessary for Trafficking Suspension Act or the PRINTS Act</strong></p><p>This bill addresses migrant minor children entering the United States. Specifically, the bill makes it a crime for a person to knowingly use a minor to gain entry to the United States if the minor is not a close relative or if the person is not the minor\u2019s guardian. In addition, U.S. Customs and Border Protection (CBP) must fingerprint all non-U.S. nationals (<em>aliens</em> under federal law) entering the United States who are younger than 14 years of age if a CBP officer suspects that the child is victim of human trafficking.</p><p>The Department of Homeland Security (DHS) must share with the Department of Health and Human Services (HHS) any fingerprints collected under this bill from an unaccompanied child if that child is transferred to HHS custody.</p><p>DHS must report to Congress on the number of children fingerprinted annually under this bill. DHS must also publish on a monthly basis the number of individuals apprehended for falsely claiming a child accompanying them into the United States was a close relative. \u00a0</p>"
        },
        "title": "PRINTS Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s53.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Preventing the Recycling of Immigrants is Necessary for Trafficking Suspension Act or the PRINTS Act</strong></p><p>This bill addresses migrant minor children entering the United States. Specifically, the bill makes it a crime for a person to knowingly use a minor to gain entry to the United States if the minor is not a close relative or if the person is not the minor\u2019s guardian. In addition, U.S. Customs and Border Protection (CBP) must fingerprint all non-U.S. nationals (<em>aliens</em> under federal law) entering the United States who are younger than 14 years of age if a CBP officer suspects that the child is victim of human trafficking.</p><p>The Department of Homeland Security (DHS) must share with the Department of Health and Human Services (HHS) any fingerprints collected under this bill from an unaccompanied child if that child is transferred to HHS custody.</p><p>DHS must report to Congress on the number of children fingerprinted annually under this bill. DHS must also publish on a monthly basis the number of individuals apprehended for falsely claiming a child accompanying them into the United States was a close relative. \u00a0</p>",
      "updateDate": "2025-03-12",
      "versionCode": "id119s53"
    },
    "title": "PRINTS Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Preventing the Recycling of Immigrants is Necessary for Trafficking Suspension Act or the PRINTS Act</strong></p><p>This bill addresses migrant minor children entering the United States. Specifically, the bill makes it a crime for a person to knowingly use a minor to gain entry to the United States if the minor is not a close relative or if the person is not the minor\u2019s guardian. In addition, U.S. Customs and Border Protection (CBP) must fingerprint all non-U.S. nationals (<em>aliens</em> under federal law) entering the United States who are younger than 14 years of age if a CBP officer suspects that the child is victim of human trafficking.</p><p>The Department of Homeland Security (DHS) must share with the Department of Health and Human Services (HHS) any fingerprints collected under this bill from an unaccompanied child if that child is transferred to HHS custody.</p><p>DHS must report to Congress on the number of children fingerprinted annually under this bill. DHS must also publish on a monthly basis the number of individuals apprehended for falsely claiming a child accompanying them into the United States was a close relative. \u00a0</p>",
      "updateDate": "2025-03-12",
      "versionCode": "id119s53"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s53is.xml"
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
      "title": "PRINTS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-11T05:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PRINTS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-11T05:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Preventing the Recycling of Immigrants is Necessary for Trafficking Suspension Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-11T05:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Homeland Security to fingerprint noncitizen minors entering the United States who are suspected of being victims of human trafficking, to require the Secretary to publicly disclose the number of such minors who are fingerprinted by U.S. Customs and Border Protection (CBP) officials and the number of child traffickers who are apprehended by CBP, to impose criminal penalties on noncitizen adults who use unrelated minors to gain entry into the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-11T05:48:29Z"
    }
  ]
}
```
