# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1789?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1789
- Title: Promptly Ending Political Prosecutions and Executive Retaliation Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1789
- Origin chamber: House
- Introduced date: 2025-03-03
- Update date: 2026-05-21T17:06:58Z
- Update date including text: 2026-05-21T17:06:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-03: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-03-05 - Committee: Committee Consideration and Mark-up Session Held
- 2025-03-05 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 14 - 11.
- 2025-03-21 - Calendars: Placed on the Union Calendar, Calendar No. 18.
- 2025-03-21 - Committee: Reported (Amended) by the Committee on Judiciary. H. Rept. 119-28.
- 2025-03-21 - Committee: Reported (Amended) by the Committee on Judiciary. H. Rept. 119-28.
- Latest action: 2025-03-03: Introduced in House

## Actions

- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-03-05 - Committee: Committee Consideration and Mark-up Session Held
- 2025-03-05 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 14 - 11.
- 2025-03-21 - Calendars: Placed on the Union Calendar, Calendar No. 18.
- 2025-03-21 - Committee: Reported (Amended) by the Committee on Judiciary. H. Rept. 119-28.
- 2025-03-21 - Committee: Reported (Amended) by the Committee on Judiciary. H. Rept. 119-28.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-03",
    "latestAction": {
      "actionDate": "2025-03-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1789",
    "number": "1789",
    "originChamber": "House",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "F000478",
        "district": "7",
        "firstName": "Russell",
        "fullName": "Rep. Fry, Russell [R-SC-7]",
        "lastName": "Fry",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "Promptly Ending Political Prosecutions and Executive Retaliation Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-21T17:06:58Z",
    "updateDateIncludingText": "2026-05-21T17:06:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H12410",
      "actionDate": "2025-03-21",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 18.",
      "type": "Calendars"
    },
    {
      "actionCode": "H12200",
      "actionDate": "2025-03-21",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Reported (Amended) by the Committee on Judiciary. H. Rept. 119-28.",
      "type": "Committee"
    },
    {
      "actionCode": "5000",
      "actionDate": "2025-03-21",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Reported (Amended) by the Committee on Judiciary. H. Rept. 119-28.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-05",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 14 - 11.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-05",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-03",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-03",
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
        "item": [
          {
            "date": "2025-03-21T20:48:50Z",
            "name": "Reported By"
          },
          {
            "date": "2025-03-05T20:16:10Z",
            "name": "Markup By"
          },
          {
            "date": "2025-03-03T17:01:40Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1789ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1789\nIN THE HOUSE OF REPRESENTATIVES\nMarch 3, 2025 Mr. Fry introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 28, United States Code, to clarify the removability of certain actions against current and former Presidents and other senior Executive officials, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Promptly Ending Political Prosecutions and Executive Retaliation Act .\n#### 2. Removal of certain actions\n##### (a) In general\nSection 1442 of title 28, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin the matter preceding paragraph (1), by inserting , upon a prima facie showing by the removing party that the standards for removal are met, after removed by them ; and\n**(B)**\nin paragraph (1)\u2014\n**(i)**\nby striking or any officer (or any person acting under that officer) of the United States or of any agency thereof, and inserting or any person who, at the time of removal, is an officer of the United States (or any person acting under that officer) or of any agency thereof, or was previously such an officer, ; and\n**(ii)**\nby inserting (including a discretionary exercise of any authority of such office) after color of such office ; and\n**(2)**\nby adding at the end of subsection (a) the following:\n(5) The President or Vice President for or relating to any act while in office or where the State court\u2019s consideration of the claim or charge may interfere with, hinder, burden, or delay the execution of the duties of the President or the Vice President. (6) A former President or Vice President for or relating to any act while in office. .\n##### (b) Application\nThe amendments made by subsection (a) shall apply to a civil action or criminal prosecution pending on the date of enactment of this Act or commenced on or after such date.\n#### 3. Procedure for removal of criminal cases\n##### (a) In general\nSection 1455(b) of title 28, United States Code, is amended\u2014\n**(1)**\nin paragraph (3)\u2014\n**(A)**\nby striking shall not and inserting shall ; and\n**(B)**\nby striking except that a judgment of conviction shall not be entered unless the prosecution is first remanded and inserting and no judgment of conviction shall be entered unless the prosecution is remanded ;\n**(2)**\nin paragraph (4), by striking promptly. If and inserting promptly and where a prima facie showing demonstrating the basis for removal is made, the matter shall be removed. Only if ; and\n**(3)**\nin paragraph (5)\u2014\n**(A)**\nby inserting summary dismissal or the after does not order the ;\n**(B)**\nby striking an evidentiary hearing and inserting a hearing ;\n**(C)**\nby inserting including dismissal under section 1456 after require ; and\n**(D)**\nby inserting or dismissal ordered after permitted .\n##### (b) Application\nThe amendments made by subsection (a) shall apply to criminal prosecutions pending on the date of enactment of this Act or commenced on or after such date.\n#### 4. Official immunity\n##### (a) In general\nChapter 89 of title 28, United States Code, is amended by adding at the end the following:\n1456. Official Immunity (a) Immunity In any case that is subject to removal under section 1442(a), a Federal official shall be presumed to have immunity under article VI, clause 2 of the Constitution of the United States from any charge or claim made by or under authority of State law which may only be rebutted by clear and convincing evidence that the official was not acting under the color of such office or on account of any right, title or authority claimed under any Act of Congress for the apprehension or punishment of criminals or the collection of the revenue. (b) Determination of immunity For purposes of making a determination of immunity under subsection (a), the following may not be admitted into evidence: (1) The nature, elements or any other aspect of the charge or claim made by or under authority of State law. (2) An act alleged to be official that is not the subject of the charge or claim made by or under authority of State law. (c) Representation In any case that is subject to removal under section 1442(a) that names a Federal official as a party, the Attorney General may\u2014 (1) represent such Federal official for any charge or claim made by or under authority of State law; or (2) compensate private counsel retained by such official at a reasonable prevailing rate for any such charge or claim. (d) Prohibition on limitation of scope No court may define or limit the scope of the duties of an official of the Executive Office of the President. (e) Dismissal In any action subject to removal under paragraph (5) or (6) of section 1442(a), such case shall be dismissed unless rebutted by clear and convincing evidence establishing that the continued pendency of the State claim or charge would not in any way interfere, hinder, burden, or delay the execution of the duties of the President or Vice President. .\n##### (b) Application\nThe amendments made by this section shall apply to civil actions or criminal prosecutions pending on the date of enactment of this Act or commenced on or after such date.",
      "versionDate": "2025-03-03",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1789rh.xml",
      "text": "IB\nUnion Calendar No. 18\n119th CONGRESS\n1st Session\nH. R. 1789\n[Report No. 119\u201328]\nIN THE HOUSE OF REPRESENTATIVES\nMarch 3, 2025 Mr. Fry introduced the following bill; which was referred to the Committee on the Judiciary\nMarch 21, 2025 Reported with an amendment, committed to the Committee of the Whole House on the State of the Union, and ordered to be printed Strike out all after the enacting clause and insert the part printed in italic For text of introduced bill, see copy of bill as introduced on March 3, 2025\nA BILL\nTo amend title 28, United States Code, to clarify the removability of certain actions against current and former Presidents and other senior Executive officials, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Promptly Ending Political Prosecutions and Executive Retaliation Act of 2025 .\n#### 2. Removal of certain actions\n##### (a) In general\nSection 1442 of title 28, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin the matter preceding paragraph (1), by inserting , upon a prima facie showing by the removing party that the standards for removal are met, after removed by them ; and\n**(B)**\nin paragraph (1)\u2014\n**(i)**\nby striking or any officer (or any person acting under that officer) of the United States or of any agency thereof, and inserting or any person who, at the time of removal, is an officer of the United States (or any person acting under that officer) or of any agency thereof, or was previously such an officer, ; and\n**(ii)**\nby inserting (including a discretionary exercise of any authority of such office) after color of such office ; and\n**(2)**\nby adding at the end of subsection (a) the following:\n(5) The President or Vice President for or relating to any act while in office or where the State court\u2019s consideration of the claim or charge may interfere with, hinder, burden, or delay the execution of the duties of the President or the Vice President. (6) A former President or Vice President for or relating to any act while in office. .\n##### (b) Application\nThe amendments made by subsection (a) shall apply to a civil action or criminal prosecution pending on the date of enactment of this Act or commenced on or after such date.\n#### 3. Procedure for removal of criminal cases\n##### (a) In general\nSection 1455(b) of title 28, United States Code, is amended\u2014\n**(1)**\nin paragraph (3)\u2014\n**(A)**\nby striking shall not and inserting shall ; and\n**(B)**\nby striking except that a judgment of conviction shall not be entered unless the prosecution is first remanded and inserting and no judgment of conviction shall be entered unless the prosecution is remanded ;\n**(2)**\nin paragraph (4), by striking promptly. If and inserting promptly and where a prima facie showing demonstrating the basis for removal is made, the matter shall be removed. Only if ; and\n**(3)**\nin paragraph (5)\u2014\n**(A)**\nby inserting summary dismissal or the after does not order the ;\n**(B)**\nby striking an evidentiary hearing and inserting a hearing ;\n**(C)**\nby inserting including dismissal under section 1456 after require ; and\n**(D)**\nby inserting or dismissal ordered after permitted .\n##### (b) Application\nThe amendments made by subsection (a) shall apply to criminal prosecutions pending on the date of enactment of this Act or commenced on or after such date.\n#### 4. Official immunity\n##### (a) In general\nChapter 89 of title 28, United States Code, is amended by adding at the end the following:\n1456. Official Immunity (a) Immunity In any case that is subject to removal under section 1442(a), a Federal official shall be presumed to have immunity under article VI, clause 2 of the Constitution of the United States from any charge or claim made by or under authority of State law which may only be rebutted by clear and convincing evidence that the official was not acting under the color of such office or on account of any right, title or authority claimed under any Act of Congress for the apprehension or punishment of criminals or the collection of the revenue. (b) Determination of immunity For purposes of making a determination of immunity under subsection (a), the following may not be admitted into evidence: (1) The nature, elements or any other aspect of the charge or claim made by or under authority of State law. (2) An act alleged to be official that is not the subject of the charge or claim made by or under authority of State law. (c) Representation In any case that is subject to removal under section 1442(a) that names a Federal official as a party, the Attorney General may\u2014 (1) represent such Federal official for any charge or claim made by or under authority of State law; or (2) compensate private counsel retained by such official at a reasonable prevailing rate for any such charge or claim. (d) Prohibition on limitation of scope No court may define or limit the scope of the duties of an official of the Executive Office of the President. (e) Dismissal In any action subject to removal under paragraph (5) or (6) of section 1442(a), such case shall be dismissed unless rebutted by clear and convincing evidence establishing that the continued pendency of the State claim or charge would not in any way interfere, hinder, burden, or delay the execution of the duties of the President or Vice President. .\n##### (b) Table of sections\nThe table of sections for such chapter is amended by adding at the end the following:\n1456. Official immunity. .\n##### (c) Application\nThe amendments made by this section shall apply to civil actions or criminal prosecutions pending on the date of enactment of this Act or commenced on or after such date.",
      "versionDate": "2025-03-21",
      "versionType": "Reported in House"
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
            "name": "Federal officials",
            "updateDate": "2025-03-25T17:10:02Z"
          },
          {
            "name": "Judicial procedure and administration",
            "updateDate": "2025-03-25T17:10:11Z"
          },
          {
            "name": "Presidents and presidential powers, Vice Presidents",
            "updateDate": "2025-03-25T17:09:55Z"
          },
          {
            "name": "State and local courts",
            "updateDate": "2025-03-25T17:10:22Z"
          }
        ]
      },
      "policyArea": {
        "name": "Law",
        "updateDate": "2026-04-16T16:05:36Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-21",
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
          "measure-id": "id119hr1789",
          "measure-number": "1789",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-21",
          "originChamber": "HOUSE",
          "update-date": "2026-05-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1789v07",
            "update-date": "2026-05-21"
          },
          "action-date": "2025-03-21",
          "action-desc": "Reported to House",
          "summary-text": "<p><strong>Promptly Ending Political Prosecutions and Executive Retaliation Act of 2025</strong></p><p>This bill expands the types of federal officials who may remove (i.e., transfer) state cases brought against them to federal court.\u00a0It also\u00a0establishes a presumption of immunity for federal officials in these cases.</p><p>The federal officer removal statute authorizes certain defendants\u00a0(e.g., federal officers) to remove to federal court a civil action or criminal prosecution brought against them in state court\u00a0if the claims or charges relate to official duties. Often, defendants who invoke the federal officer removal statute raise claims of official immunity.</p><p>In recent years, the statute received public attention when then-former President Donald Trump and former officials sought to invoke the statute. For example, in <em>Georgia v. Meadows</em>, the U.S. Court of Appeals for the Eleventh Circuit\u00a0held that former White House Chief of Staff Mark Meadows could not remove Georgia\u2019s criminal prosecution of him to federal court based on the federal officer removal statute because it does not apply to former federal officers, and even if it did, the charges were not related to Meadows\u2019s official duties.</p><p>This bill allows\u00a0a defendant\u00a0who is a former federal officer\u00a0or current or former President or Vice President\u00a0to remove state cases brought against them to federal court based on the federal officer removal statute.\u00a0It\u00a0also establishes a presumption that federal officials have immunity in cases that are removable, which may only be rebutted by a showing that their actions were not related to official duties.</p>"
        },
        "title": "Promptly Ending Political Prosecutions and Executive Retaliation Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1789.xml",
    "summary": {
      "actionDate": "2025-03-21",
      "actionDesc": "Reported to House",
      "text": "<p><strong>Promptly Ending Political Prosecutions and Executive Retaliation Act of 2025</strong></p><p>This bill expands the types of federal officials who may remove (i.e., transfer) state cases brought against them to federal court.\u00a0It also\u00a0establishes a presumption of immunity for federal officials in these cases.</p><p>The federal officer removal statute authorizes certain defendants\u00a0(e.g., federal officers) to remove to federal court a civil action or criminal prosecution brought against them in state court\u00a0if the claims or charges relate to official duties. Often, defendants who invoke the federal officer removal statute raise claims of official immunity.</p><p>In recent years, the statute received public attention when then-former President Donald Trump and former officials sought to invoke the statute. For example, in <em>Georgia v. Meadows</em>, the U.S. Court of Appeals for the Eleventh Circuit\u00a0held that former White House Chief of Staff Mark Meadows could not remove Georgia\u2019s criminal prosecution of him to federal court based on the federal officer removal statute because it does not apply to former federal officers, and even if it did, the charges were not related to Meadows\u2019s official duties.</p><p>This bill allows\u00a0a defendant\u00a0who is a former federal officer\u00a0or current or former President or Vice President\u00a0to remove state cases brought against them to federal court based on the federal officer removal statute.\u00a0It\u00a0also establishes a presumption that federal officials have immunity in cases that are removable, which may only be rebutted by a showing that their actions were not related to official duties.</p>",
      "updateDate": "2026-05-21",
      "versionCode": "id119hr1789"
    },
    "title": "Promptly Ending Political Prosecutions and Executive Retaliation Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-21",
      "actionDesc": "Reported to House",
      "text": "<p><strong>Promptly Ending Political Prosecutions and Executive Retaliation Act of 2025</strong></p><p>This bill expands the types of federal officials who may remove (i.e., transfer) state cases brought against them to federal court.\u00a0It also\u00a0establishes a presumption of immunity for federal officials in these cases.</p><p>The federal officer removal statute authorizes certain defendants\u00a0(e.g., federal officers) to remove to federal court a civil action or criminal prosecution brought against them in state court\u00a0if the claims or charges relate to official duties. Often, defendants who invoke the federal officer removal statute raise claims of official immunity.</p><p>In recent years, the statute received public attention when then-former President Donald Trump and former officials sought to invoke the statute. For example, in <em>Georgia v. Meadows</em>, the U.S. Court of Appeals for the Eleventh Circuit\u00a0held that former White House Chief of Staff Mark Meadows could not remove Georgia\u2019s criminal prosecution of him to federal court based on the federal officer removal statute because it does not apply to former federal officers, and even if it did, the charges were not related to Meadows\u2019s official duties.</p><p>This bill allows\u00a0a defendant\u00a0who is a former federal officer\u00a0or current or former President or Vice President\u00a0to remove state cases brought against them to federal court based on the federal officer removal statute.\u00a0It\u00a0also establishes a presumption that federal officials have immunity in cases that are removable, which may only be rebutted by a showing that their actions were not related to official duties.</p>",
      "updateDate": "2026-05-21",
      "versionCode": "id119hr1789"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1789ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2025-03-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1789rh.xml"
        }
      ],
      "type": "Reported in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Promptly Ending Political Prosecutions and Executive Retaliation Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-22T06:08:20Z"
    },
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "Promptly Ending Political Prosecutions and Executive Retaliation Act of 2025",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2025-03-22T06:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Promptly Ending Political Prosecutions and Executive Retaliation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T04:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 28, United States Code, to clarify the removability of certain actions against current and former Presidents and other senior Executive officials, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T04:19:25Z"
    }
  ]
}
```
