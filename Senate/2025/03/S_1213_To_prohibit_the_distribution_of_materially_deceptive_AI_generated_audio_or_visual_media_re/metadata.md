# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1213?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1213
- Title: Protect Elections from Deceptive AI Act
- Congress: 119
- Bill type: S
- Bill number: 1213
- Origin chamber: Senate
- Introduced date: 2025-03-31
- Update date: 2025-12-05T21:39:24Z
- Update date including text: 2025-12-05T21:39:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-31: Introduced in Senate
- 2025-03-31 - IntroReferral: Introduced in Senate
- 2025-03-31 - IntroReferral: Read twice and referred to the Committee on Rules and Administration.
- Latest action: 2025-03-31: Introduced in Senate

## Actions

- 2025-03-31 - IntroReferral: Introduced in Senate
- 2025-03-31 - IntroReferral: Read twice and referred to the Committee on Rules and Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-31",
    "latestAction": {
      "actionDate": "2025-03-31",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1213",
    "number": "1213",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "K000367",
        "district": "",
        "firstName": "Amy",
        "fullName": "Sen. Klobuchar, Amy [D-MN]",
        "lastName": "Klobuchar",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "Protect Elections from Deceptive AI Act",
    "type": "S",
    "updateDate": "2025-12-05T21:39:24Z",
    "updateDateIncludingText": "2025-12-05T21:39:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-31",
      "committees": {
        "item": {
          "name": "Rules and Administration Committee",
          "systemCode": "ssra00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Rules and Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-31",
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
          "date": "2025-03-31T21:44:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Rules and Administration Committee",
      "systemCode": "ssra00",
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
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "MO"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "DE"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "ME"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1213is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1213\nIN THE SENATE OF THE UNITED STATES\nMarch 31, 2025 Ms. Klobuchar (for herself, Mr. Hawley , Mr. Coons , Ms. Collins , and Mr. Bennet ) introduced the following bill; which was read twice and referred to the Committee on Rules and Administration\nA BILL\nTo prohibit the distribution of materially deceptive AI-generated audio or visual media relating to candidates for Federal office, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protect Elections from Deceptive AI Act .\n#### 2. Prohibition on distribution of materially deceptive AI-generated audio or visual media prior to election\n##### (a) In general\nTitle III of the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30101 et seq. ) is amended by adding at the end the following new section:\n325. Prohibition on distribution of materially deceptive AI-generated audio or visual media (a) Definitions In this section: (1) Covered individual The term covered individual means a candidate for Federal office. (2) Deceptive AI-generated audio or visual media The term deceptive AI-generated audio or visual media means an image, audio, or video that\u2014 (A) is the product of artificial intelligence technology that uses machine learning (including deep learning models, natural learning processing, or any other computational processing techniques of similar or greater complexity), that\u2014 (i) merges, combines, replaces, or superimposes content onto an image, audio, or video, creating an image, audio, or video that appears authentic; or (ii) generates an inauthentic image, audio, or video that appears authentic; and (B) a reasonable person, having considered the qualities of the image, audio, or video and the nature of the distribution channel in which the image, audio, or video appears\u2014 (i) would have a fundamentally different understanding or impression of the appearance, speech, or expressive conduct exhibited in the image, audio, or video than that person would have if that person were hearing or seeing the unaltered, original version of the image, audio, or video; or (ii) would believe that the image, audio, or video accurately exhibits any appearance, speech, or expressive conduct of a person who did not actually exhibit such appearance, speech, or expressive conduct. (3) Federal election activity The term Federal election activity has the meaning given the term in section 301(20)(A)(iii). (b) Prohibition Except as provided in subsection (c), a person, political committee, or other entity may not knowingly distribute materially deceptive AI-generated audio or visual media in carrying out a Federal election activity or of a covered individual for the purpose of\u2014 (1) influencing an election; or (2) soliciting funds. (c) Inapplicability to certain entities This section shall not apply to the following: (1) A radio or television broadcasting station, including a cable or satellite television operator, programmer, or producer, or a streaming service that broadcasts materially deceptive AI-generated audio or visual media prohibited by this section as part of a bona fide newscast, news interview, news documentary, or on-the-spot coverage of bona fide news events, if the broadcast clearly acknowledges through content or a disclosure, in a manner that can be easily heard or read by the average listener or viewer, that there are questions about the authenticity of the materially deceptive AI-generated audio or visual media. (2) A regularly published newspaper, magazine, or other periodical of general circulation, including an internet or electronic publication, that routinely carries news and commentary of general interest, and that publishes materially deceptive AI-generated audio or visual media prohibited under this section, if the publication clearly states that the materially deceptive AI-generated audio or visual media does not accurately represent the speech or conduct of the covered individual. (3) Materially deceptive AI-generated audio or visual media that constitutes satire or parody. (d) Civil action (1) Injunctive or other equitable relief (A) In general A covered individual whose voice or likeness appears in, or who is the subject of, a materially deceptive AI-generated audio or visual media, including content distributed as part of a Federal election activity, distributed in violation of this section may seek injunctive or other equitable relief prohibiting the distribution of materially deceptive AI-generated audio or visual media in violation of this section. (B) Precedence An action under this paragraph shall be entitled to precedence in accordance with the Federal Rules of Civil Procedure. (2) Damages (A) In general A covered individual whose voice or likeness appears in, or who is the subject of, a materially deceptive AI-generated audio or visual media, including content distributed as part of a Federal election activity, distributed in violation of this section may bring an action for general or special damages against the person, committee, or other entity that distributed the materially deceptive AI-generated audio or visual media. (B) Attorney's fees and costs In addition to any damages awarded under subparagraph (A), the court may also award a prevailing party reasonable attorney\u2019s fees and costs. (C) Rule of construction Nothing in this paragraph shall be construed to limit or preclude a plaintiff from securing or recovering any other available remedy. (3) Burden of proof In any civil action alleging a violation of this section, the plaintiff shall bear the burden of establishing the violation through clear and convincing evidence. .\n##### (b) Severability\nIf any provision of this Act, or an amendment made by this Act, or the application of such provision to any person or circumstance, is held to be invalid, the remainder of this Act, or an amendment made by this Act, or the application of such provision to other persons or circumstances, shall not be affected.",
      "versionDate": "2025-03-31",
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
        "actionDate": "2025-09-10",
        "text": "Referred to the House Committee on House Administration."
      },
      "number": "5272",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Protect Elections from Deceptive AI Act",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-09T16:15:18Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-31",
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
          "measure-id": "id119s1213",
          "measure-number": "1213",
          "measure-type": "s",
          "orig-publish-date": "2025-03-31",
          "originChamber": "SENATE",
          "update-date": "2025-07-01"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1213v00",
            "update-date": "2025-07-01"
          },
          "action-date": "2025-03-31",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Protect Elections from Deceptive AI Act</strong></p><p>This bill prohibits the distribution of materially deceptive audio or visual media that is generated by artificial intelligence (AI) relating to federal candidates.</p><p>The bill generally prohibits individuals, political committees, and other entities from knowingly distributing materially deceptive AI-generated audio or visual media in carrying out a federal election activity or of a federal candidate for the purpose of\u00a0(1) influencing an election, or (2) soliciting funds. This prohibition does not apply to certain entities, such as radio or television broadcasting stations that broadcast such media with disclosures as part of a bona fide newscast.</p><p>The bill also permits a federal candidate whose voice or likeness appears in such materially deceptive AI-generated audio or visual media to bring a civil action for injunctive relief or damages.</p>"
        },
        "title": "Protect Elections from Deceptive AI Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1213.xml",
    "summary": {
      "actionDate": "2025-03-31",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protect Elections from Deceptive AI Act</strong></p><p>This bill prohibits the distribution of materially deceptive audio or visual media that is generated by artificial intelligence (AI) relating to federal candidates.</p><p>The bill generally prohibits individuals, political committees, and other entities from knowingly distributing materially deceptive AI-generated audio or visual media in carrying out a federal election activity or of a federal candidate for the purpose of\u00a0(1) influencing an election, or (2) soliciting funds. This prohibition does not apply to certain entities, such as radio or television broadcasting stations that broadcast such media with disclosures as part of a bona fide newscast.</p><p>The bill also permits a federal candidate whose voice or likeness appears in such materially deceptive AI-generated audio or visual media to bring a civil action for injunctive relief or damages.</p>",
      "updateDate": "2025-07-01",
      "versionCode": "id119s1213"
    },
    "title": "Protect Elections from Deceptive AI Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-31",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protect Elections from Deceptive AI Act</strong></p><p>This bill prohibits the distribution of materially deceptive audio or visual media that is generated by artificial intelligence (AI) relating to federal candidates.</p><p>The bill generally prohibits individuals, political committees, and other entities from knowingly distributing materially deceptive AI-generated audio or visual media in carrying out a federal election activity or of a federal candidate for the purpose of\u00a0(1) influencing an election, or (2) soliciting funds. This prohibition does not apply to certain entities, such as radio or television broadcasting stations that broadcast such media with disclosures as part of a bona fide newscast.</p><p>The bill also permits a federal candidate whose voice or likeness appears in such materially deceptive AI-generated audio or visual media to bring a civil action for injunctive relief or damages.</p>",
      "updateDate": "2025-07-01",
      "versionCode": "id119s1213"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1213is.xml"
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
      "title": "Protect Elections from Deceptive AI Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-15T04:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protect Elections from Deceptive AI Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-15T04:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit the distribution of materially deceptive AI-generated audio or visual media relating to candidates for Federal office, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-15T04:19:08Z"
    }
  ]
}
```
