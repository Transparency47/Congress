# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4161?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4161
- Title: Maverick Act
- Congress: 119
- Bill type: S
- Bill number: 4161
- Origin chamber: Senate
- Introduced date: 2026-03-23
- Update date: 2026-05-19T21:41:06Z
- Update date including text: 2026-05-19T21:41:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, amendments, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2026-03-23: Introduced in Senate
- 2026-03-23 - IntroReferral: Introduced in Senate
- 2026-03-23 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- 2026-04-28 - Floor: Measure laid before Senate by unanimous consent. (consideration: CR S2075)
- 2026-04-28 - Floor: Passed Senate with an amendment by Unanimous Consent. (text: CR S2075)
- 2026-04-28 - Floor: Passed/agreed to in Senate: Passed Senate with an amendment by Unanimous Consent.
- 2026-04-28 - Discharge: Senate Committee on Armed Services discharged by Unanimous Consent.
- 2026-04-28 - Committee: Senate Committee on Armed Services discharged by Unanimous Consent.
- 2026-05-01 - Floor: Message on Senate action sent to the House.
- 2026-05-04 10:32:46 - Floor: Received in the House.
- 2026-05-04 10:33:00 - Floor: Held at the desk.
- Latest action: 2026-03-23: Introduced in Senate

## Actions

- 2026-03-23 - IntroReferral: Introduced in Senate
- 2026-03-23 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- 2026-04-28 - Floor: Measure laid before Senate by unanimous consent. (consideration: CR S2075)
- 2026-04-28 - Floor: Passed Senate with an amendment by Unanimous Consent. (text: CR S2075)
- 2026-04-28 - Floor: Passed/agreed to in Senate: Passed Senate with an amendment by Unanimous Consent.
- 2026-04-28 - Discharge: Senate Committee on Armed Services discharged by Unanimous Consent.
- 2026-04-28 - Committee: Senate Committee on Armed Services discharged by Unanimous Consent.
- 2026-05-01 - Floor: Message on Senate action sent to the House.
- 2026-05-04 10:32:46 - Floor: Received in the House.
- 2026-05-04 10:33:00 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-23",
    "latestAction": {
      "actionDate": "2026-03-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4161",
    "number": "4161",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S001232",
        "district": "",
        "firstName": "Tim",
        "fullName": "Sen. Sheehy, Tim [R-MT]",
        "lastName": "Sheehy",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "Maverick Act",
    "type": "S",
    "updateDate": "2026-05-19T21:41:06Z",
    "updateDateIncludingText": "2026-05-19T21:41:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2026-05-04",
      "actionTime": "10:33:00",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2026-05-04",
      "actionTime": "10:32:46",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-05-01",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-04-28",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate with an amendment by Unanimous Consent. (text: CR S2075)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2026-04-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate with an amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-04-28",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Measure laid before Senate by unanimous consent. (consideration: CR S2075)",
      "type": "Floor"
    },
    {
      "actionDate": "2026-04-28",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on Armed Services discharged by Unanimous Consent.",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2026-04-28",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on Armed Services discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-23",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-23",
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

## API Data: amendments

```json
{
  "amendments": [
    {
      "amendment": {
        "actions": {
          "actions": {
            "item": [
              {
                "actionDate": "2026-04-28",
                "sourceSystem": {
                  "code": "0",
                  "name": "Senate"
                },
                "text": "Amendment SA 5437 agreed to in Senate by Unanimous Consent.",
                "type": "Floor"
              },
              {
                "actionDate": "2026-04-28",
                "sourceSystem": {
                  "code": "0",
                  "name": "Senate"
                },
                "text": "Amendment SA 5437 proposed by Senator Lummis for Senator Scott FL. (consideration: CR S2075)",
                "type": "Floor"
              },
              {
                "actionCode": "Intro-S",
                "actionDate": "2026-04-28",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "type": "IntroReferral"
              },
              {
                "actionCode": "93000",
                "actionDate": "2026-04-28",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "text": "Senate amendment proposed (on the floor): Amendment SA 5437 proposed by Senator Lummis for Senator Scott FL.",
                "type": "Floor"
              },
              {
                "actionCode": "91000",
                "actionDate": "2026-04-28",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "text": "Senate amendment submitted",
                "type": "Floor"
              },
              {
                "actionCode": "94000",
                "actionDate": "2026-04-28",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "text": "Senate amendment agreed to: Amendment SA 5437 agreed to in Senate by Unanimous Consent.",
                "type": "Floor"
              }
            ]
          },
          "count": "6"
        },
        "amendedBill": {
          "congress": "119",
          "number": "4161",
          "originChamber": "Senate",
          "originChamberCode": "S",
          "title": "Maverick Act",
          "type": "S",
          "updateDateIncludingText": "2026-05-19"
        },
        "chamber": "Senate",
        "congress": "119",
        "latestAction": {
          "actionDate": "2026-04-28",
          "links": {
            "link": {
              "name": "SA 5437",
              "url": "https://www.congress.gov/amendment/119th-congress/senate-amendment/5437"
            }
          },
          "text": "Amendment SA 5437 agreed to in Senate by Unanimous Consent."
        },
        "number": "5437",
        "onBehalfOfSponsor": {
          "item": [
            {
              "bioguideId": "L000571",
              "firstName": "Cynthia",
              "fullName": "Rep. Lummis, Cynthia M. [R-WY-At Large]",
              "lastName": "Lummis",
              "party": "R",
              "state": "WY",
              "type": "Submitted on behalf of"
            },
            {
              "bioguideId": "L000571",
              "firstName": "Cynthia",
              "fullName": "Rep. Lummis, Cynthia M. [R-WY-At Large]",
              "lastName": "Lummis",
              "party": "R",
              "state": "WY",
              "type": "Proposed on behalf of"
            }
          ]
        },
        "proposedDate": "2026-04-28T04:00:00Z",
        "purpose": "To clarify the provision of excess spare parts to the Commission.",
        "sponsors": {
          "item": {
            "bioguideId": "S001217",
            "firstName": "Rick",
            "fullName": "Sen. Scott, Rick [R-FL]",
            "lastName": "Scott",
            "party": "R",
            "state": "FL"
          }
        },
        "submittedDate": "2026-04-28T04:00:00Z",
        "textVersions": {
          "count": "1"
        },
        "type": "SAMDT",
        "updateDate": "2026-04-30T11:08:23Z"
      }
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
            "date": "2026-04-28T22:50:55Z",
            "name": "Discharged From"
          },
          {
            "date": "2026-03-23T20:06:28Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2026-03-23",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4161is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4161\nIN THE SENATE OF THE UNITED STATES\nMarch 23, 2026 Mr. Sheehy (for himself and Mr. Kelly ) introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo authorize the transfer by the Secretary of the Navy to the U.S. Space and Rocket Center Commission in Huntsville, Alabama, of certain F\u201314 Tomcat aircraft.\n#### 1. Short title\nThis Act may be cited as the Maverick Act .\n#### 2. Conveyance of F\u201314D Tomcat aircraft from the Navy to the U.S. Space and rocket center commission in Huntsville, Alabama\n##### (a) Authority\nThe Secretary of the Navy (in this section referred to as the Secretary ) may convey, without consideration, to the U.S. Space and Rocket Center Commission in Huntsville, Alabama (in this section referred to as the Commission ), all right, title, and interest of the United States in and to 3 surplus F\u201314D Tomcat aircraft (Bureau Numbers 164341, 164602, 159437), which are excess to the operational requirements of the Navy.\n##### (b) Form of conveyance\nThe conveyance under subsection (a) shall be made by means of a conditional deed of gift.\n##### (c) Condition of aircraft\nThe aircraft being conveyed under subsection (a) do not have any capability for use as a platform for launching or releasing munitions or any other combat capability that it was designed to have.\n##### (d) Conditions\nThe Secretary shall include in the instrument of conveyance of the aircraft under subsection (a)\u2014\n**(1)**\na condition that the Secretary is not required to repair or alter the condition of the aircraft before conveying ownership of the aircraft;\n**(2)**\na condition that the Secretary shall provide any maintenance and operations manuals that\u2014\n**(A)**\nare specific to the F\u201314D aircraft; and\n**(B)**\nthe Secretary has sufficient intellectual property rights to convey;\n**(3)**\na condition that the Secretary shall provide excess spare parts to make one of the F\u201314D aircraft flyable or able to complete a static display, provided that any part transferred is from existing Navy stock, with no items being procured on behalf of the Commission; and\n**(4)**\na condition that the Secretary will not be responsible for transferring any additional parts or providing any additional support beyond what is stated in this section, during or after the conveyance of the aircraft.\n##### (e) Agreements for restoration and operation\nThe Secretary may\u2014\n**(1)**\nauthorize the Commission to enter into agreements with qualified nonprofit organizations for the purpose of restoring and operating the aircraft transferred under subsection (a) for public display, airshows, and commemorative events to preserve naval aviation heritage; and\n**(2)**\nif the Secretary authorizes any such agreement, require such additional terms and conditions in the instrument of conveyance as appropriate to protect the interests of the United States.\n##### (f) Reverter upon breach of conditions\nThe Secretary shall include in the instrument of conveyance of the aircraft under subsection (a)\u2014\n**(1)**\na condition that the Commission shall operate and maintain the aircraft in compliance with all applicable limitations and maintenance requirements imposed by the Administrator of the Federal Aviation Administration;\n**(2)**\na condition that the Commission shall not convey any ownership interest in, or transfer possession of, the aircraft to another party without the prior approval of the Secretary; and\n**(3)**\na condition that if the Secretary determines at any time that the Commission has failed to comply with the conditions set forth in paragraphs (1) and (2), all right, title, and interest in and to the aircraft, including any repair or alteration of the aircraft, shall revert to the United States, and the United States shall have the right of immediate possession of the aircraft.\n##### (g) Conveyance at no cost to the United States\nThe conveyance of an aircraft under subsection (a) shall be made at no cost to the United States. Any costs associated with such conveyance, costs of determining compliance with terms of the conveyance, and costs of operation and maintenance of the aircraft conveyed shall be borne by the Commission.\n##### (h) Clarification of liability\nNotwithstanding any other provision of law, upon the conveyance of ownership of the aircraft under subsection (a), the United States shall not be liable for any death, injury, loss, or damage that results from any use of such aircraft by any person other than the United States.\n##### (i) Applicable law\nThe transfer and use of the aircraft under subsection (a) is subject to all applicable Federal and State laws and regulations, including\u2014\n**(1)**\nthe Arms Control Act ( 22 U.S.C. 2751 et seq. );\n**(2)**\nthe Export Control Reform Act of 2018 ( 50 U.S.C. 4811 et seq. );\n**(3)**\nInternational Traffic in Arms Regulations (22 CFR 120 et seq.);\n**(4)**\nExport Administration Regulations (15 CFR 730 et seq.);\n**(5)**\nForeign Assets Control Regulations (31 CFR 500 et seq.); and\n**(6)**\nchapter 37 of title 18, United States Code (commonly known as the Espionage Act ).",
      "versionDate": "2026-03-23",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4161es.xml",
      "text": "119th CONGRESS\n2d Session\nS. 4161\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo authorize the transfer by the Secretary of the Navy to the U.S. Space and Rocket Center Commission in Huntsville, Alabama, of certain F\u201314 Tomcat aircraft.\n#### 1. Short title\nThis Act may be cited as the Maverick Act .\n#### 2. Conveyance of F\u201314D Tomcat aircraft from the Navy to the U.S. Space and rocket center commission in Huntsville, Alabama\n##### (a) Authority\nThe Secretary of the Navy (in this section referred to as the Secretary ) may convey, without consideration, to the U.S. Space and Rocket Center Commission in Huntsville, Alabama (in this section referred to as the Commission ), all right, title, and interest of the United States in and to 3 surplus F\u201314D Tomcat aircraft (Bureau Numbers 164341, 164602, 159437), which are excess to the operational requirements of the Navy.\n##### (b) Form of conveyance\nThe conveyance under subsection (a) shall be made by means of a conditional deed of gift.\n##### (c) Condition of aircraft\nThe aircraft being conveyed under subsection (a) do not have any capability for use as a platform for launching or releasing munitions or any other combat capability that it was designed to have.\n##### (d) Conditions\nThe Secretary shall include in the instrument of conveyance of the aircraft under subsection (a)\u2014\n**(1)**\na condition that the Secretary is not required to repair or alter the condition of the aircraft before conveying ownership of the aircraft;\n**(2)**\na condition that the Secretary shall provide any maintenance and operations manuals that\u2014\n**(A)**\nare specific to the F\u201314D aircraft; and\n**(B)**\nthe Secretary has sufficient intellectual property rights to convey;\n**(3)**\na condition that the Secretary may provide excess spare parts to make one of the F\u201314D aircraft flyable or able to complete a static display, provided that any part transferred from existing Navy stock is replenished at fair market value by the Commission, with no items being procured by the Secretary on behalf of the Commission; and\n**(4)**\na condition that the Secretary will not be responsible for transferring any additional parts or providing any additional support beyond what is stated in this section, during or after the conveyance of the aircraft.\n##### (e) Agreements for restoration and operation\nThe Secretary may\u2014\n**(1)**\nauthorize the Commission to enter into agreements with qualified nonprofit organizations for the purpose of restoring and operating the aircraft transferred under subsection (a) for public display, airshows, and commemorative events to preserve naval aviation heritage; and\n**(2)**\nif the Secretary authorizes any such agreement, require such additional terms and conditions in the instrument of conveyance as appropriate to protect the interests of the United States.\n##### (f) Reverter upon breach of conditions\nThe Secretary shall include in the instrument of conveyance of the aircraft under subsection (a)\u2014\n**(1)**\na condition that the Commission shall operate and maintain the aircraft in compliance with all applicable limitations and maintenance requirements imposed by the Administrator of the Federal Aviation Administration;\n**(2)**\na condition that the Commission shall not convey any ownership interest in, or transfer possession of, the aircraft to another party without the prior approval of the Secretary; and\n**(3)**\na condition that if the Secretary determines at any time that the Commission has failed to comply with the conditions set forth in paragraphs (1) and (2), all right, title, and interest in and to the aircraft, including any repair or alteration of the aircraft, shall revert to the United States, and the United States shall have the right of immediate possession of the aircraft.\n##### (g) Conveyance at no cost to the United States\nThe conveyance of an aircraft under subsection (a) shall be made at no cost to the United States. Any costs associated with such conveyance, costs of determining compliance with terms of the conveyance, and costs of operation and maintenance of the aircraft conveyed shall be borne by the Commission.\n##### (h) Clarification of liability\nNotwithstanding any other provision of law, upon the conveyance of ownership of the aircraft under subsection (a), the United States shall not be liable for any death, injury, loss, or damage that results from any use of such aircraft by any person other than the United States.\n##### (i) Applicable law\nThe transfer and use of the aircraft under subsection (a) is subject to all applicable Federal and State laws and regulations, including\u2014\n**(1)**\nthe Arms Control Act ( 22 U.S.C. 2751 et seq. );\n**(2)**\nthe Export Control Reform Act of 2018 ( 50 U.S.C. 4811 et seq. );\n**(3)**\nInternational Traffic in Arms Regulations (22 CFR 120 et seq.);\n**(4)**\nExport Administration Regulations (15 CFR 730 et seq.);\n**(5)**\nForeign Assets Control Regulations (31 CFR 500 et seq.); and\n**(6)**\nchapter 37 of title 18, United States Code (commonly known as the Espionage Act ).",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
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
            "name": "Alabama",
            "updateDate": "2026-05-04T14:05:05Z"
          },
          {
            "name": "Aviation and airports",
            "updateDate": "2026-05-04T13:43:42Z"
          },
          {
            "name": "Military history",
            "updateDate": "2026-05-04T14:04:57Z"
          },
          {
            "name": "Museums, exhibitions, cultural centers",
            "updateDate": "2026-05-04T14:04:28Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2026-05-04T19:41:54Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-04-28",
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
          "measure-id": "id119s4161",
          "measure-number": "4161",
          "measure-type": "s",
          "orig-publish-date": "2026-04-28",
          "originChamber": "SENATE",
          "update-date": "2026-05-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s4161v55",
            "update-date": "2026-05-19"
          },
          "action-date": "2026-04-28",
          "action-desc": "Passed Senate",
          "summary-text": "<p><strong>Maverick Act</strong></p><p>This bill authorizes the Department of the Navy to transfer three surplus F-14D Tomcat aircraft to the U.S. Space and Rocket Center Commission in Huntsville, Alabama. (The F-14D Tomcat was a naval fighter aircraft that was retired from service in 2006.)</p><p>The bill provides for certain conditions for the transfer, including that the transfer must be free of cost to the federal government. Additionally, the commission must not convey ownership interest in the aircraft to another party without Navy approval. If the commission breaches any conditions, the aircraft must revert to the United States.</p><p>The bill also specifies that such aircraft may not have any combat capability. The Navy may provide excess spare parts to the commission to make one of the aircraft flyable or complete for a static display.</p><p>The Navy may authorize the commission to enter into agreements with qualified\u00a0nonprofit\u00a0organizations to restore and operate the aircraft for public display, air shows, and commemorative events.</p>"
        },
        "title": "Maverick Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s4161.xml",
    "summary": {
      "actionDate": "2026-04-28",
      "actionDesc": "Passed Senate",
      "text": "<p><strong>Maverick Act</strong></p><p>This bill authorizes the Department of the Navy to transfer three surplus F-14D Tomcat aircraft to the U.S. Space and Rocket Center Commission in Huntsville, Alabama. (The F-14D Tomcat was a naval fighter aircraft that was retired from service in 2006.)</p><p>The bill provides for certain conditions for the transfer, including that the transfer must be free of cost to the federal government. Additionally, the commission must not convey ownership interest in the aircraft to another party without Navy approval. If the commission breaches any conditions, the aircraft must revert to the United States.</p><p>The bill also specifies that such aircraft may not have any combat capability. The Navy may provide excess spare parts to the commission to make one of the aircraft flyable or complete for a static display.</p><p>The Navy may authorize the commission to enter into agreements with qualified\u00a0nonprofit\u00a0organizations to restore and operate the aircraft for public display, air shows, and commemorative events.</p>",
      "updateDate": "2026-05-19",
      "versionCode": "id119s4161"
    },
    "title": "Maverick Act"
  },
  "summaries": [
    {
      "actionDate": "2026-04-28",
      "actionDesc": "Passed Senate",
      "text": "<p><strong>Maverick Act</strong></p><p>This bill authorizes the Department of the Navy to transfer three surplus F-14D Tomcat aircraft to the U.S. Space and Rocket Center Commission in Huntsville, Alabama. (The F-14D Tomcat was a naval fighter aircraft that was retired from service in 2006.)</p><p>The bill provides for certain conditions for the transfer, including that the transfer must be free of cost to the federal government. Additionally, the commission must not convey ownership interest in the aircraft to another party without Navy approval. If the commission breaches any conditions, the aircraft must revert to the United States.</p><p>The bill also specifies that such aircraft may not have any combat capability. The Navy may provide excess spare parts to the commission to make one of the aircraft flyable or complete for a static display.</p><p>The Navy may authorize the commission to enter into agreements with qualified\u00a0nonprofit\u00a0organizations to restore and operate the aircraft for public display, air shows, and commemorative events.</p>",
      "updateDate": "2026-05-19",
      "versionCode": "id119s4161"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-03-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4161is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4161es.xml"
        }
      ],
      "type": "Engrossed in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Maverick Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-02T11:03:25Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Maverick Act",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2026-04-29T04:53:33Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Maverick Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-03T05:38:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to authorize the transfer by the Secretary of the Navy to the U.S. Space and Rocket Center Commission in Huntsville, Alabama, of certain F-14 Tomcat aircraft.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-03T05:33:32Z"
    }
  ]
}
```
