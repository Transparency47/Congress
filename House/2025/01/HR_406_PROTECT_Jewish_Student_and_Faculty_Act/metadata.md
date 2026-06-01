# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/406?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/406
- Title: PROTECT Jewish Student and Faculty Act
- Congress: 119
- Bill type: HR
- Bill number: 406
- Origin chamber: House
- Introduced date: 2025-01-15
- Update date: 2025-07-21T19:44:15Z
- Update date including text: 2025-07-21T19:44:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-15: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-01-15: Introduced in House

## Actions

- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-15",
    "latestAction": {
      "actionDate": "2025-01-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/406",
    "number": "406",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "Y000067",
        "district": "2",
        "firstName": "Rudy",
        "fullName": "Rep. Yakym, Rudy [R-IN-2]",
        "lastName": "Yakym",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "PROTECT Jewish Student and Faculty Act",
    "type": "HR",
    "updateDate": "2025-07-21T19:44:15Z",
    "updateDateIncludingText": "2025-07-21T19:44:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-15",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-15",
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
          "date": "2025-01-15T15:07:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-01-15",
      "state": "MI"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "AZ"
    },
    {
      "bioguideId": "B001260",
      "district": "16",
      "firstName": "Vern",
      "fullName": "Rep. Buchanan, Vern [R-FL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Buchanan",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "FL"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "PA"
    },
    {
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "SC"
    },
    {
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "NY"
    },
    {
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "UT"
    },
    {
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2025-07-14",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr406ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 406\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2025 Mr. Yakym (for himself and Ms. Scholten ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Higher Education Act of 1965 to require institutions of higher education, as a condition of participation in programs under title IV of such Act, to include a prohibition of antisemitic conduct in all documents relating to student or employee conduct.\n#### 1. Short title\nThis Act may be cited as the Promote Restoring Order To End Campus Targeting of Jewish Students and Faculty Act or the PROTECT Jewish Student and Faculty Act .\n#### 2. Prohibition of antisemitic conduct\nSection 487(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1094(a) ) is amended by adding at the end the following:\n(30) The institution will include, in all documents and other resources relating to student or employee conduct on campus\u2014 (A) a definition of antisemitism which states that\u2014 (i) antisemitism is a certain perception of Jews, which may be expressed as hatred toward Jews; and (ii) rhetorical and physical manifestations of antisemitism may be directed toward\u2014 (I) Jewish or non-Jewish individuals, including the property of such individuals; and (II) Jewish community institutions and religious facilities; and (B) a statement that antisemitic conduct is prohibited on campus, and that such conduct\u2014 (i) by a student may result in the expulsion of the student from the institution; and (ii) by an employee may result in the termination of the employee\u2019s employment at the institution. .",
      "versionDate": "2025-01-15",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Higher education",
            "updateDate": "2025-02-27T15:20:40Z"
          },
          {
            "name": "Racial and ethnic relations",
            "updateDate": "2025-02-27T15:20:50Z"
          },
          {
            "name": "Religion",
            "updateDate": "2025-02-27T15:20:45Z"
          },
          {
            "name": "School administration",
            "updateDate": "2025-02-27T15:20:54Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-02-11T13:21:41Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-15",
    "originChamber": "House",
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
          "measure-id": "id119hr406",
          "measure-number": "406",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-15",
          "originChamber": "HOUSE",
          "update-date": "2025-03-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr406v00",
            "update-date": "2025-03-14"
          },
          "action-date": "2025-01-15",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Promote Restoring Order To End Campus Targeting of Jewish Students and Faculty Act or the PROTECT Jewish Student and Faculty Act</strong></p><p>This bill requires institutions of higher education (IHEs) that participate in federal student aid programs to adopt a standard definition of anti-Semitism in their student and employee codes of conduct and prohibit such conduct on campus.</p><p>Specifically, the IHE must include in its documents related to student and employee conduct a definition of\u00a0anti-Semitism which states that (1)\u00a0anti-Semitism is a certain perception of Jews, which may be expressed as hatred toward Jews; and (2) rhetorical and physical manifestations of anti-Semitism may be directed toward Jewish or non-Jewish individuals, including the property of such individuals, and Jewish community institutions and religious facilities. (This definition is the same as the working definition of anti-Semitism from the International Holocaust Remembrance Alliance.)</p><p>Additionally, the IHE must include in such documents a statement that\u00a0anti-Semitic conduct is prohibited on campus and that such conduct may result in expulsion or termination of employment.</p>"
        },
        "title": "PROTECT Jewish Student and Faculty Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr406.xml",
    "summary": {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Promote Restoring Order To End Campus Targeting of Jewish Students and Faculty Act or the PROTECT Jewish Student and Faculty Act</strong></p><p>This bill requires institutions of higher education (IHEs) that participate in federal student aid programs to adopt a standard definition of anti-Semitism in their student and employee codes of conduct and prohibit such conduct on campus.</p><p>Specifically, the IHE must include in its documents related to student and employee conduct a definition of\u00a0anti-Semitism which states that (1)\u00a0anti-Semitism is a certain perception of Jews, which may be expressed as hatred toward Jews; and (2) rhetorical and physical manifestations of anti-Semitism may be directed toward Jewish or non-Jewish individuals, including the property of such individuals, and Jewish community institutions and religious facilities. (This definition is the same as the working definition of anti-Semitism from the International Holocaust Remembrance Alliance.)</p><p>Additionally, the IHE must include in such documents a statement that\u00a0anti-Semitic conduct is prohibited on campus and that such conduct may result in expulsion or termination of employment.</p>",
      "updateDate": "2025-03-14",
      "versionCode": "id119hr406"
    },
    "title": "PROTECT Jewish Student and Faculty Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Promote Restoring Order To End Campus Targeting of Jewish Students and Faculty Act or the PROTECT Jewish Student and Faculty Act</strong></p><p>This bill requires institutions of higher education (IHEs) that participate in federal student aid programs to adopt a standard definition of anti-Semitism in their student and employee codes of conduct and prohibit such conduct on campus.</p><p>Specifically, the IHE must include in its documents related to student and employee conduct a definition of\u00a0anti-Semitism which states that (1)\u00a0anti-Semitism is a certain perception of Jews, which may be expressed as hatred toward Jews; and (2) rhetorical and physical manifestations of anti-Semitism may be directed toward Jewish or non-Jewish individuals, including the property of such individuals, and Jewish community institutions and religious facilities. (This definition is the same as the working definition of anti-Semitism from the International Holocaust Remembrance Alliance.)</p><p>Additionally, the IHE must include in such documents a statement that\u00a0anti-Semitic conduct is prohibited on campus and that such conduct may result in expulsion or termination of employment.</p>",
      "updateDate": "2025-03-14",
      "versionCode": "id119hr406"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr406ih.xml"
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
      "title": "PROTECT Jewish Student and Faculty Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-08T05:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PROTECT Jewish Student and Faculty Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-08T05:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Promote Restoring Order To End Campus Targeting of Jewish Students and Faculty Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-08T05:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Higher Education Act of 1965 to require institutions of higher education, as a condition of participation in programs under title IV of such Act, to include a prohibition of antisemitic conduct in all documents relating to student or employee conduct.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-08T05:48:28Z"
    }
  ]
}
```
