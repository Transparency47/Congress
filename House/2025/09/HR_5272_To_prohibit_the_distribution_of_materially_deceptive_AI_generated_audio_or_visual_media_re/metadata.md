# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5272?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5272
- Title: Protect Elections from Deceptive AI Act
- Congress: 119
- Bill type: HR
- Bill number: 5272
- Origin chamber: House
- Introduced date: 2025-09-10
- Update date: 2026-04-10T08:06:14Z
- Update date including text: 2026-04-10T08:06:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-10: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Referred to the House Committee on House Administration.
- Latest action: 2025-09-10: Introduced in House

## Actions

- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Referred to the House Committee on House Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-10",
    "latestAction": {
      "actionDate": "2025-09-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5272",
    "number": "5272",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "J000310",
        "district": "32",
        "firstName": "Julie",
        "fullName": "Rep. Johnson, Julie [D-TX-32]",
        "lastName": "Johnson",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "Protect Elections from Deceptive AI Act",
    "type": "HR",
    "updateDate": "2026-04-10T08:06:14Z",
    "updateDateIncludingText": "2026-04-10T08:06:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-10",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-10",
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
          "date": "2025-09-10T14:02:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "PA"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "PA"
    },
    {
      "bioguideId": "G000594",
      "district": "23",
      "firstName": "Tony",
      "fullName": "Rep. Gonzales, Tony [R-TX-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Gonzales",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "TX"
    },
    {
      "bioguideId": "A000379",
      "district": "4",
      "firstName": "Mark",
      "fullName": "Rep. Alford, Mark [R-MO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Alford",
      "party": "R",
      "sponsorshipDate": "2026-04-09",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5272ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5272\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 10, 2025 Ms. Johnson of Texas (for herself, Mr. Fitzpatrick , Ms. Houlahan , and Mr. Tony Gonzales of Texas ) introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo prohibit the distribution of materially deceptive AI-generated audio or visual media relating to candidates for Federal office, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protect Elections from Deceptive AI Act .\n#### 2. Prohibition on distribution of materially deceptive AI-generated audio or visual media prior to election\n##### (a) In general\nTitle III of the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30101 et seq. ) is amended by adding at the end the following new section:\n325. Prohibition on distribution of materially deceptive AI-generated audio or visual media (a) Definitions In this section: (1) Covered individual The term covered individual means a candidate for Federal office. (2) Deceptive AI-generated audio or visual media The term deceptive AI-generated audio or visual media means an image, audio, or video that\u2014 (A) is the product of artificial intelligence or machine learning, including deep learning techniques, that\u2014 (i) merges, combines, replaces, or superimposes content onto an image, audio, or video, creating an image, audio, or video that appears authentic; or (ii) generates an inauthentic image, audio, or video that appears authentic; and (B) a reasonable person, having considered the qualities of the image, audio, or video and the nature of the distribution channel in which the image, audio, or video appears\u2014 (i) would have a fundamentally different understanding or impression of the appearance, speech, or expressive conduct exhibited in the image, audio, or video than that person would have if that person were hearing or seeing the unaltered, original version of the image, audio, or video; or (ii) would believe that the image, audio, or video accurately exhibits any appearance, speech, or expressive conduct of a person who did not actually exhibit such appearance, speech, or expressive conduct. (3) Federal election activity The term Federal election activity has the meaning given the term in section 301(20)(A)(iii). (b) Prohibition Except as provided in subsection (c), a person, political committee, or other entity may not knowingly distribute materially deceptive AI-generated audio or visual media of a covered individual, or in carrying out a Federal election activity, with the intent to\u2014 (1) influence an election; or (2) solicit funds. (c) Inapplicability to certain entities This section shall not apply to the following: (1) A radio or television broadcasting station, including a cable or satellite television operator, programmer, or producer, or a streaming service that broadcasts materially deceptive AI-generated audio or visual media prohibited by this section as part of a bona fide newscast, news interview, news documentary, or on-the-spot coverage of bona fide news events, if the broadcast clearly acknowledges through content or a disclosure, in a manner that can be easily heard or read by the average listener or viewer, that there are questions about the authenticity of the materially deceptive AI-generated audio or visual media. (2) A regularly published newspaper, magazine, or other periodical of general circulation, including an internet or electronic publication, that routinely carries news and commentary of general interest, and that publishes materially deceptive AI-generated audio or visual media prohibited under this section, if the publication clearly states that the materially deceptive AI-generated audio or visual media does not accurately represent the speech or conduct of the covered individual. (3) Materially deceptive AI-generated audio or visual media that constitutes satire or parody. (d) Civil action (1) Injunctive or other equitable relief (A) In general A covered individual whose voice or likeness appears in, or who is the subject of, a materially deceptive AI-generated audio or visual media, including content distributed as part of a Federal election activity, distributed in violation of this section may seek injunctive or other equitable relief prohibiting the distribution of materially deceptive AI-generated audio or visual media in violation of this section. (B) Precedence An action under this paragraph shall be entitled to precedence in accordance with the Federal Rules of Civil Procedure. (2) Damages (A) In general A covered individual whose voice or likeness appears in, or who is the subject of, a materially deceptive AI-generated audio or visual media, including content distributed as part of a Federal election activity, distributed in violation of this section may bring an action for general or special damages against the person, committee, or other entity that distributed the materially deceptive AI-generated audio or visual media. (B) Attorney\u2019s fees and costs In addition to any damages awarded under subparagraph (A), the court may also award a prevailing party reasonable attorney\u2019s fees and costs. (C) Rule of construction Nothing in this paragraph shall be construed to limit or preclude a plaintiff from securing or recovering any other available remedy. (3) Burden of proof In any civil action alleging a violation of this section, the plaintiff shall bear the burden of establishing the violation through clear and convincing evidence. .\n##### (b) Effect on defamation action\nFor purposes of an action for defamation, a violation of section 325 of the Federal Election Campaign Act of 1971, as added by subsection (a), shall constitute defamation per se.\n##### (c) Severability\nIf any provision of this Act, or an amendment made by this Act, or the application of such provision to any person or circumstance, is held to be invalid, the remainder of this Act, or an amendment made by this Act, or the application of such provision to other persons or circumstances, shall not be affected.",
      "versionDate": "2025-09-10",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-03-31",
        "text": "Read twice and referred to the Committee on Rules and Administration."
      },
      "number": "1213",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Protect Elections from Deceptive AI Act",
      "type": "S"
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
        "updateDate": "2025-09-24T15:14:07Z"
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
      "date": "2025-09-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5272ih.xml"
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
      "title": "Protect Elections from Deceptive AI Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-18T04:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protect Elections from Deceptive AI Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-18T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the distribution of materially deceptive AI-generated audio or visual media relating to candidates for Federal office, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-18T04:18:29Z"
    }
  ]
}
```
