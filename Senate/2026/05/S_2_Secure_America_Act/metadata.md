# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2
- Title: Secure America Act
- Congress: 119
- Bill type: S
- Bill number: 2
- Origin chamber: Senate
- Introduced date: 2026-05-20
- Update date: 2026-05-22T11:08:30Z
- Update date including text: 2026-05-22T11:08:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, amendments, committees, fullTexts, text, titles

## Timeline

- 2026-05-20: Introduced in Senate
- 2026-05-20 - Committee: Committee on the Budget. Original measure reported to Senate by Senator Graham. Without written report.
- 2026-05-20 - Committee: Committee on the Budget. Original measure reported to Senate by Senator Graham. Without written report.
- 2026-05-20 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 417.
- Latest action: 2026-05-20: Committee on the Budget. Original measure reported to Senate by Senator Graham. Without written report.

## Actions

- 2026-05-20 - Committee: Committee on the Budget. Original measure reported to Senate by Senator Graham. Without written report.
- 2026-05-20 - Committee: Committee on the Budget. Original measure reported to Senate by Senator Graham. Without written report.
- 2026-05-20 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 417.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-20",
    "latestAction": {
      "actionDate": "2026-05-20",
      "text": "Committee on the Budget. Original measure reported to Senate by Senator Graham. Without written report."
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2",
    "number": "2",
    "originChamber": "Senate",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "G000359",
        "district": "",
        "firstName": "Lindsey",
        "fullName": "Sen. Graham, Lindsey [R-SC]",
        "lastName": "Graham",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "Secure America Act",
    "type": "S",
    "updateDate": "2026-05-22T11:08:30Z",
    "updateDateIncludingText": "2026-05-22T11:08:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-20",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 417.",
      "type": "Calendars"
    },
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Budget Committee",
          "systemCode": "ssbu00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on the Budget. Original measure reported to Senate by Senator Graham. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Budget Committee",
          "systemCode": "ssbu00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on the Budget. Original measure reported to Senate by Senator Graham. Without written report.",
      "type": "Committee"
    }
  ]
}
```

## API Data: amendments

```json
{
  "amendments": [
    {
      "amendment": [
        {
          "actions": {
            "actions": {
              "item": [
                {
                  "actionCode": "Intro-S",
                  "actionDate": "2026-05-21",
                  "sourceSystem": {
                    "code": "9",
                    "name": "Library of Congress"
                  },
                  "type": "IntroReferral"
                },
                {
                  "actionCode": "91000",
                  "actionDate": "2026-05-21",
                  "sourceSystem": {
                    "code": "9",
                    "name": "Library of Congress"
                  },
                  "text": "Senate amendment submitted",
                  "type": "Floor"
                }
              ]
            },
            "count": "2"
          },
          "amendedBill": {
            "congress": "119",
            "number": "2",
            "originChamber": "Senate",
            "originChamberCode": "S",
            "title": "Secure America Act",
            "type": "S",
            "updateDateIncludingText": "2026-05-22"
          },
          "chamber": "Senate",
          "congress": "119",
          "number": "5450",
          "sponsors": {
            "item": {
              "bioguideId": "M001153",
              "firstName": "Lisa",
              "fullName": "Sen. Murkowski, Lisa [R-AK]",
              "lastName": "Murkowski",
              "party": "R",
              "state": "AK"
            }
          },
          "submittedDate": "2026-05-21T04:00:00Z",
          "type": "SAMDT",
          "updateDate": "2026-05-22T11:08:30Z"
        },
        {
          "actions": {
            "actions": {
              "item": [
                {
                  "actionCode": "Intro-S",
                  "actionDate": "2026-05-21",
                  "sourceSystem": {
                    "code": "9",
                    "name": "Library of Congress"
                  },
                  "type": "IntroReferral"
                },
                {
                  "actionCode": "91000",
                  "actionDate": "2026-05-21",
                  "sourceSystem": {
                    "code": "9",
                    "name": "Library of Congress"
                  },
                  "text": "Senate amendment submitted",
                  "type": "Floor"
                }
              ]
            },
            "count": "2"
          },
          "amendedBill": {
            "congress": "119",
            "number": "2",
            "originChamber": "Senate",
            "originChamberCode": "S",
            "title": "Secure America Act",
            "type": "S",
            "updateDateIncludingText": "2026-05-22"
          },
          "chamber": "Senate",
          "congress": "119",
          "number": "5449",
          "sponsors": {
            "item": {
              "bioguideId": "M001153",
              "firstName": "Lisa",
              "fullName": "Sen. Murkowski, Lisa [R-AK]",
              "lastName": "Murkowski",
              "party": "R",
              "state": "AK"
            }
          },
          "submittedDate": "2026-05-21T04:00:00Z",
          "type": "SAMDT",
          "updateDate": "2026-05-22T11:08:30Z"
        },
        {
          "actions": {
            "actions": {
              "item": [
                {
                  "actionCode": "Intro-S",
                  "actionDate": "2026-05-21",
                  "sourceSystem": {
                    "code": "9",
                    "name": "Library of Congress"
                  },
                  "type": "IntroReferral"
                },
                {
                  "actionCode": "91000",
                  "actionDate": "2026-05-21",
                  "sourceSystem": {
                    "code": "9",
                    "name": "Library of Congress"
                  },
                  "text": "Senate amendment submitted",
                  "type": "Floor"
                }
              ]
            },
            "count": "2"
          },
          "amendedBill": {
            "congress": "119",
            "number": "2",
            "originChamber": "Senate",
            "originChamberCode": "S",
            "title": "Secure America Act",
            "type": "S",
            "updateDateIncludingText": "2026-05-22"
          },
          "chamber": "Senate",
          "congress": "119",
          "number": "5448",
          "sponsors": {
            "item": {
              "bioguideId": "M001153",
              "firstName": "Lisa",
              "fullName": "Sen. Murkowski, Lisa [R-AK]",
              "lastName": "Murkowski",
              "party": "R",
              "state": "AK"
            }
          },
          "submittedDate": "2026-05-21T04:00:00Z",
          "type": "SAMDT",
          "updateDate": "2026-05-22T11:08:30Z"
        },
        {
          "actions": {
            "actions": {
              "item": [
                {
                  "actionCode": "Intro-S",
                  "actionDate": "2026-05-21",
                  "sourceSystem": {
                    "code": "9",
                    "name": "Library of Congress"
                  },
                  "type": "IntroReferral"
                },
                {
                  "actionCode": "91000",
                  "actionDate": "2026-05-21",
                  "sourceSystem": {
                    "code": "9",
                    "name": "Library of Congress"
                  },
                  "text": "Senate amendment submitted",
                  "type": "Floor"
                }
              ]
            },
            "count": "2"
          },
          "amendedBill": {
            "congress": "119",
            "number": "2",
            "originChamber": "Senate",
            "originChamberCode": "S",
            "title": "Secure America Act",
            "type": "S",
            "updateDateIncludingText": "2026-05-22"
          },
          "chamber": "Senate",
          "congress": "119",
          "number": "5447",
          "sponsors": {
            "item": {
              "bioguideId": "S000033",
              "firstName": "Bernie",
              "fullName": "Sen. Sanders, Bernard [I-VT]",
              "lastName": "Sanders",
              "party": "I",
              "state": "VT"
            }
          },
          "submittedDate": "2026-05-21T04:00:00Z",
          "type": "SAMDT",
          "updateDate": "2026-05-22T11:08:29Z"
        },
        {
          "actions": {
            "actions": {
              "item": [
                {
                  "actionCode": "Intro-S",
                  "actionDate": "2026-05-21",
                  "sourceSystem": {
                    "code": "9",
                    "name": "Library of Congress"
                  },
                  "type": "IntroReferral"
                },
                {
                  "actionCode": "91000",
                  "actionDate": "2026-05-21",
                  "sourceSystem": {
                    "code": "9",
                    "name": "Library of Congress"
                  },
                  "text": "Senate amendment submitted",
                  "type": "Floor"
                }
              ]
            },
            "count": "2"
          },
          "amendedBill": {
            "congress": "119",
            "number": "2",
            "originChamber": "Senate",
            "originChamberCode": "S",
            "title": "Secure America Act",
            "type": "S",
            "updateDateIncludingText": "2026-05-22"
          },
          "chamber": "Senate",
          "congress": "119",
          "number": "5446",
          "sponsors": {
            "item": {
              "bioguideId": "B001267",
              "firstName": "Michael",
              "fullName": "Sen. Bennet, Michael F. [D-CO]",
              "lastName": "Bennet",
              "party": "D",
              "state": "CO"
            }
          },
          "submittedDate": "2026-05-21T04:00:00Z",
          "type": "SAMDT",
          "updateDate": "2026-05-22T11:08:29Z"
        },
        {
          "actions": {
            "actions": {
              "item": [
                {
                  "actionCode": "Intro-S",
                  "actionDate": "2026-05-20",
                  "sourceSystem": {
                    "code": "9",
                    "name": "Library of Congress"
                  },
                  "type": "IntroReferral"
                },
                {
                  "actionCode": "91000",
                  "actionDate": "2026-05-20",
                  "sourceSystem": {
                    "code": "9",
                    "name": "Library of Congress"
                  },
                  "text": "Senate amendment submitted",
                  "type": "Floor"
                }
              ]
            },
            "count": "2"
          },
          "amendedBill": {
            "congress": "119",
            "number": "2",
            "originChamber": "Senate",
            "originChamberCode": "S",
            "title": "Secure America Act",
            "type": "S",
            "updateDateIncludingText": "2026-05-22"
          },
          "chamber": "Senate",
          "congress": "119",
          "number": "5443",
          "sponsors": {
            "item": {
              "bioguideId": "C001075",
              "firstName": "Bill",
              "fullName": "Sen. Cassidy, Bill [R-LA]",
              "lastName": "Cassidy",
              "party": "R",
              "state": "LA"
            }
          },
          "submittedDate": "2026-05-20T04:00:00Z",
          "type": "SAMDT",
          "updateDate": "2026-05-21T11:08:29Z"
        }
      ]
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
          "date": "2026-05-20T14:52:46Z",
          "name": "Reported Original Measure"
        }
      },
      "chamber": "Senate",
      "name": "Budget Committee",
      "systemCode": "ssbu00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s2pcs.xml",
      "text": "II\nCalendar No. 417\n119th CONGRESS\n2d Session\nS. 2\nIN THE SENATE OF THE UNITED STATES\nMay 20, 2026 Mr. Graham , from the Committee on the Budget , reported the following original bill; which was read twice and placed on the calendar\nA BILL\nTo provide for reconciliation pursuant to title II of S. Con. Res. 33.\n#### 1. Short title\nThis Act may be cited as the Secure America Act .\nI\nCommittee on Homeland Security and Governmental Affairs\n#### 101. U.S. Customs and Border Protection personnel\n##### (a) Personnel\nIn addition to amounts otherwise available, there is appropriated to the Commissioner of U.S. Customs and Border Protection for fiscal year 2026, out of any money in the Treasury not otherwise appropriated, $9,550,000,000, to remain available until September 30, 2029, to hire, pay, train, and equip Border Patrol agents and Border Patrol support personnel to conduct functions other than immigration enforcement and customs functions.\n##### (b) Restriction\nNone of the funds made available by subsection (a) may be used to recruit, hire, or train personnel for the duties of processing coordinators after October 31, 2028.\n#### 102. U.S. Immigration and Customs Enforcement\nIn addition to amounts otherwise available, there is appropriated to the Director of U.S. Immigration and Customs Enforcement for fiscal year 2026, out of any money in the Treasury not otherwise appropriated, $7,450,000,000, to remain available until September 30, 2029, to hire, pay, train, and equip Homeland Security Investigations agents and support personnel and to provide other necessary expenses for Homeland Security Investigations\u2019 mission support and operations and maintenance, of which $108,500,000 shall be used to hire, pay, and equip additional child exploitation investigators and forensics analysts at the Victim Identification Laboratory of the Child Exploitation Investigations Unit of Homeland Security Investigations and at the Homeland Security Investigations offices of the Special Agent in Charge to support the identification and rescue of victims of child sexual exploitation and abuse, and to train such personnel and State and local law enforcement regarding identifying victims of child sexual exploitation and abuse within the Homeland Security Investigations Cyber Crimes Center, except that funds provided in this section shall be used for functions other than those related to Homeland Security Investigations\u2019 immigration enforcement and customs enforcement missions.\n#### 103. Border security, technology, and screening\n##### (a) In general\nIn addition to amounts otherwise available, there is appropriated to the Commissioner of U.S. Customs and Border Protection for fiscal year 2026, out of any money in the Treasury not otherwise appropriated, to remain available until September 30, 2029, $3,450,000,000 for the following:\n**(1)**\nProcurement and integration of new nonintrusive inspection equipment and associated civil works, including artificial intelligence, machine learning, and other innovative technologies, as well as other mission support, to combat the entry or exit of illicit narcotics at ports of entry and along the southwest, northern, and maritime borders.\n**(2)**\nAir and Marine operations\u2019 upgrading and procurement of new platforms for rapid air and marine response capabilities.\n**(3)**\nUpgrades and procurement of border surveillance technologies along the southwest, northern, and maritime borders.\n**(4)**\nNecessary expenses, including the deployment of technology, relating to the biometric entry and exit system under section 7208 of the Intelligence Reform and Terrorism Prevention Act of 2004 ( 8 U.S.C. 1365b ).\n**(5)**\nEnhancing border security by combating drug trafficking, including fentanyl and its precursor chemicals, at the southwest, northern, and maritime borders.\n**(6)**\nNecessary expenses for U.S. Customs and Border Protection's mission support and operations and maintenance for functions other than those related to its immigration enforcement and customs missions.\n##### (b) Restrictions\nNone of the funds made available under subsection (a) may be used for the procurement or deployment of surveillance towers along the southwest border and northern border that have not been tested and accepted by U.S. Customs and Border Protection to deliver autonomous capabilities.\n##### (c) Definition of autonomous\nIn this section, with respect to capabilities, the term autonomous means a system designed to apply artificial intelligence, machine learning, computer vision, or other algorithms to accurately detect, identify, classify, and track items of interest in real time such that the system can make operational adjustments without the active engagement of personnel or continuous human command or control.\n#### 104. Additional Department of Homeland Security appropriations\nIn addition to amounts otherwise available, there are appropriated to the Secretary of Homeland Security for fiscal year 2026, out of any money in the Treasury not otherwise appropriated, $2,500,000,000, to remain available until September 30, 2029, for the purposes provided in this title.",
      "versionDate": "2025-05-20",
      "versionType": "Placed on Calendar Senate"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s2pcs.xml"
        }
      ],
      "type": "Placed on Calendar Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Secure America Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-21T17:08:33Z"
    },
    {
      "billTextVersionCode": "PCS",
      "billTextVersionName": "Placed on Calendar Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Secure America Act",
      "titleType": "Short Title(s) from PCS (Placed on Senate Calendar) bill text",
      "titleTypeCode": "152",
      "updateDate": "2026-05-21T17:08:33Z"
    },
    {
      "title": "An original bill to provide for reconciliation pursuant to title II of S. Con. Res. 33.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-21T10:56:36Z"
    }
  ]
}
```
