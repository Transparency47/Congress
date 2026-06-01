# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1119?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1119
- Title: Impeaching Pamela Bondi, Attorney General of the United States, for high crimes and misdemeanors.
- Congress: 119
- Bill type: HRES
- Bill number: 1119
- Origin chamber: House
- Introduced date: 2026-03-17
- Update date: 2026-03-20T08:06:42Z
- Update date including text: 2026-03-20T08:06:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-17: Introduced in House
- 2026-03-17 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2026-03-17 - IntroReferral: Submitted in House
- 2026-03-17 - IntroReferral: Submitted in House
- Latest action: 2026-03-17: Submitted in House

## Actions

- 2026-03-17 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2026-03-17 - IntroReferral: Submitted in House
- 2026-03-17 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-17",
    "latestAction": {
      "actionDate": "2026-03-17",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1119",
    "number": "1119",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "L000602",
        "district": "12",
        "firstName": "Summer",
        "fullName": "Rep. Lee, Summer L. [D-PA-12]",
        "lastName": "Lee",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Impeaching Pamela Bondi, Attorney General of the United States, for high crimes and misdemeanors.",
    "type": "HRES",
    "updateDate": "2026-03-20T08:06:42Z",
    "updateDateIncludingText": "2026-03-20T08:06:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-17",
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
      "actionCode": "H11100",
      "actionDate": "2026-03-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-03-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2026-03-17T14:00:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "NC"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "AZ"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "True",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "CA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "MI"
    },
    {
      "bioguideId": "D000635",
      "district": "3",
      "firstName": "Maxine",
      "fullName": "Rep. Dexter, Maxine [D-OR-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Dexter",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "OR"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
      "state": "NM"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1119ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1119\nIN THE HOUSE OF REPRESENTATIVES\nMarch 17, 2026 Ms. Lee of Pennsylvania (for herself, Mrs. Foushee , Ms. Ansari , Mr. Min , Ms. Tlaib , and Ms. Dexter ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nImpeaching Pamela Bondi, Attorney General of the United States, for high crimes and misdemeanors.\nThat Pamela Bondi, Attorney General of the United States, is impeached for high crimes and misdemeanors, and that the following articles of impeachment be exhibited to the Senate:\nArticles of impeachment exhibited by the House of Representatives of the United States of America in the name of itself and of the people of the United States of America, against Pamela Bondi, Attorney General of the United States of America, in maintenance and support of its impeachment against her for high crimes and misdemeanors.\n#### Article I: Obstruction of Congress\u2014Defiance of subpoena\nIn her conduct of the office of Attorney General of the United States, Pamela Bondi, contrary to her oath faithfully to execute the office of Attorney General of the United States and, to the best of her ability preserve, protect, and defend the Constitution of the United States, and in violation of her constitutional duty to take care that the laws be faithfully executed, has failed without lawful cause or excuse to produce the materials, papers, and things contained in the Jeffrey Epstein files, as directed by the duly authorized subpoena issued to the U.S. Department of Justice by the House Committee on Oversight and Government Reform on August 5, 2025, and willfully disobeyed such subpoena. The Epstein files contain information related to convicted sex offender Jeffrey Epstein and was deemed necessary by the Committee in order to resolve fundamental, factual questions relating to Jeffrey Epstein\u2019s ties with political leaders and other influential figures; and to their knowledge of, participation in, or cover up of Jeffrey Epstein\u2019s sexual abuse, assault, and trafficking of children and women. The Department of Justice refused to adhere to the subpoena and withheld substantial evidence; evidence logs indicate that amongst the withheld evidence are FBI interviews with a survivor who accuses Trump of sexual abuse. In refusing to produce the whole and unredacted Epstein files and the materials, documents, and other things contained therein, Pamela Bondi, substituting her judgment as to what materials were necessary for the inquiry of Congress, interposed the powers of the Department of Justice against the lawful subpoena of the House of Representatives, thereby assuming to herself functions and judgments necessary to the exercise of powers vested by the Constitution in the House of Representatives. In so doing, Pamela Bondi knowingly and intentionally abused the power of her office to shield individuals named in the Epstein files such as political leaders and other influential individuals, including Donald J. Trump, from accountability and oversight by Congress. In all of this, Pamela Bondi has acted in a manner contrary to her trust as Attorney General and subversive of constitutional government, to the great prejudice of the cause of law and justice, and to the manifest injury of the people of the United States. Wherefore, Pamela Bondi, by such conduct, warrants impeachment and trial, and removal from office.\n#### ARTICLE II: OBSTRUCTION OF CONGRESS\u2014DEFIANCE OF THE EPSTEIN FILES TRANSPARENCY ACT\nIn her conduct of the office of Attorney General of the United States, Pamela Bondi, contrary to her oath faithfully to execute the office of Attorney General of the United States and, to the best of her ability preserve, protect, and defend the Constitution of the United States, and in violation of her constitutional duty to take care that the laws be faithfully executed, has failed without lawful cause or excuse to adhere to the Epstein Files Transparency Act (EFTA), which was signed into law on November 19, 2025, by Donald J. Trump after it passed with a veto-proof majority of votes in Congress. The EFTA requires Ms. Bondi, as Attorney General with authority over the Epstein files in control of the U.S. Department of Justice (DOJ), to produce all unclassified records, documents, communications, and investigative materials in the possession of the Department of Justice, including the Federal Bureau of Investigation and United States Attorneys\u2019 Offices, that relate to Jeffrey Epstein and Ghislaine Maxwell; and prohibits Ms. Bondi from withholding, delaying, or redacting documents on the basis of embarrassment, reputational harm, or political sensitivity, including to any government official, public figure, or foreign dignitary. Ms. Bondi refused to adhere to the EFTA\u2019s December 19, 2025, statutory deadline for disclosure. The purportedly final trove of documents released by the DOJ in January 2025 contained 3 million pages of documents. Many of these documents were heavily redacted and the DOJ continues to withhold documents, including communications from and involving Ms. Bondi and other officials within Donald J. Trump\u2019s administration. Evidence logs indicate that amongst the withheld evidence are FBI interviews with a survivor who accuses Trump of sexual abuse. But while Ms. Bondi continues to defy the law in a manner that protects political leaders and other influential individuals, including Donald J. Trump himself, she failed to protect the victims. Although the only permissible redactions authorized by the law were intended to protect the victims, Ms. Bondi instead released at least dozens of sensitive documents, including nude photographs and personally identifiable information of Epstein\u2019s victims. In refusing to produce the Epstein files and the materials, documents, and other things contained therein, in failing to adhere to the redaction guidance provided by Congress that was intended to facilitate the protection of Epstein\u2019s victims, and instead redacting and withholding the documents in such a manner as to protect herself, Donald J. Trump, and other influential members or allies of the Trump administration, Pamela Bondi interposed the powers of the Department of Justice against the laws of this country. In so doing, Pamela Bondi knowingly and intentionally abused the power of her office to shield individuals named in the Epstein files, including but not limited to Donald J. Trump, from accountability and oversight by Congress, and demonstrated gross incompetence in failing to protect Epstein\u2019s victims. In all of this, Pamela Bondi has acted in a manner contrary to her trust as Attorney General and subversive of constitutional government, to the great prejudice of the cause of law and justice, and to the manifest injury of the people of the United States. Wherefore, Pamela Bondi, by such conduct, warrants impeachment and trial, and removal from office.\n#### ARTICLE III: ABUSE OF INVESTIGATORY AND PROSECUTORIAL POWERS\nIn her conduct of the office of Attorney General of the United States, Pamela Bondi, contrary to her oath faithfully to execute the office of Attorney General of the United States and, to the best of her ability preserve, protect, and defend the Constitution of the United States, and in violation of her constitutional duty to take care that the laws be faithfully executed, has engaged in conduct that impaired the due and proper administration of justice and the conduct of lawful inquiries and has violated the constitutional right of citizens and residents of this country. She has, acting personally and through her subordinates and agents, abused the investigatory and prosecutorial powers of the Department of Justice and the Federal Bureau of Investigation to pursue partisan interests to the detriment of the country; to enable corruption; to protect Donald J. Trump and his allies from oversight and criminal prosecution; to undermine the security and reliability of U.S. elections; and to support his anti-democratic assault on state rights, protesters, free speech, and immigrants. The means used to implement this course of conduct or plan included one or more of the following, carried out personally and through her subordinates and agents:\n**(1)**\nShe terminated without cause the Director of the Departmental Ethics Office, who is tasked with overseeing ethics compliance across the Department of Justice.\n**(2)**\nShe terminated career public servants in the Department of Justice and the Federal Bureau of Investigation for carrying out their duties and fulfilling the obligations of their office as they pertained to investigations and prosecutions that she and Trump disfavor, including investigations and prosecutions into the crimes committed by Trump himself, Trump\u2019s allies, Jeffrey Epstein, and people who carried out the January 6, 2021, attack on the U.S. Capitol. These terminations not only rid these critically important institutions of nonpartisan career public servants, they demonstrated to remaining employees that they would be subject to politically motivated retribution if they carry out their jobs ethically and in a nonpartisan manner.\n**(3)**\nShe has ordered and orchestrated politically motivated and abusive investigations into Trump\u2019s political opponents or other individuals disfavored by Trump, including former FBI Director James Comey, New York Attorney General Letitia James, California senator Adam Schiff, Federal Reserve Chair Jerome Powell, and Federal Reserve Board of Governors Member Lisa Cook, as well as against six members of Congress who made a video that truthfully informed military servicemembers that they do not have to obey unlawful orders. Her baseless indictments against Comey and James were both dismissed, and a grand jury refused to indict the six members of Congress. Dozens of high-ranking, career prosecutors and investigators have quit rather than pursue baseless and politically motivated investigations.\n**(4)**\nShe has closed investigations and dismissed lawsuits and prosecutions into Trump, his allies, and individuals with personal connections to her and others within the Trump administration, including but not limited to: an investigation into Tom Homan\u2019s retention of $50,000 cash from an FBI investigation in 2024; dismissing corruption charges against former New York City Mayor Eric Adams for what the chief prosecutor on the case said, in resigning from her position, was driven by improper considerations ; dismissing with prejudice a discrimination lawsuit brought by the DOJ against Musk\u2019s SpaceX in 2023 for its refusal to hire refugees and people granted asylum in the United States, in violation of Federal law; dismissing fraud charges mid-trial against a doctor who was accused of falsifying COVID\u201319 vaccination cards and destroying government-supplied vaccines; dismissing charges against defendants represented by her own brother; dismissing charges against The Boeing Company over the two passenger jet crashes that killed 346 people in Indonesia and Ethiopia; and ending enforcement of foreign corruption cases, including a long-standing investigation into her own former client, Pfizer.\n**(5)**\nShe has abused the power of her office to target and punish journalists in violation of the First Amendment, including by arresting and prosecuting journalist Don Lemon and orchestrating a raid on the home of Washington Post reporter Hannah Natanson.\n**(6)**\nShe has abused the power of her office to prosecute protesters for engaging in protected speech and acts in protest of the administration\u2019s immigration policies and further has violated the DOJ\u2019s own policies by publicly sharing the names and photographs of protesters her office has arrested, which has served an unconstitutional and dangerous chilling effect on the expression of free speech in this country.\n**(7)**\nShe is abusing laws intended to protect Americans from domestic terrorism, turning them into mechanisms by which Federal law enforcement and the Department of Justice are unlawfully and unconstitutionally targeting, harassing, and persecuting individuals and organizations who hold viewpoints with which Trump disagrees. She has directed Federal law enforcement agencies to define domestic terrorism threat as Antifa aligned extremists, which in turn she defines as individuals and entities who hold and express ideas with which the Trump administration disagrees, namely extreme viewpoints on immigration, radical gender ideology, and anti-American sentiment. She further has ordered Federal law enforcement agencies to create and maintain secret lists of organizations and individuals that purportedly meet this criteria; to create hotlines by which people can be anonymously reported for their anti-Trump ideologies; and to prioritize the tracking, investigation, and prosecution of these entities and individuals, all of which directly undermine the safety and security of American residents and citizens, turn Federal resources toward the unlawful surveillance and persecution of people on the basis of their protected right to beliefs and speech.\n**(8)**\nShe orchestrated and carried out a raid on Fulton County\u2019s election office and seizing thousands of Fulton County election records, including hundreds of thousands of ballots and other records that contain sensitive voter information, purportedly as part of Trump\u2019s scheme to undermine and challenge the 2020 election.\n**(9)**\nShe has abused the power of her office to assist Trump in undermining the security and reliability of U.S. elections, including by bringing baseless lawsuits demanding that states turn over their voter rolls; demanding that Minnesota Governor Tim Walz turn over the state\u2019s voter information in exchange for ending the violent occupation of the city by Federal immigration officials, who have already murdered two civilians and have injured, threatened, and harassed countless more; and creating Memorandums of Understandings that require states to surrender control over their voter lists and give the Federal Government the ability to carry out purges with no mechanism for the state or the voters to contest these purges.\nIn all this, Pamela Bondi has\n                acted in a manner contrary to her trust as Attorney General and subversive of\n                constitutional government, to the great prejudice of the cause of law and justice\n                and to the manifest injury of the people of the United States. Wherefore Pamela\n                Bondi, by such conduct, warrants impeachment and trial, and removal from\n                office.\n#### ARTICLE IV: DISMANTLING THE RULE OF LAW THROUGH DEFIANCE OF THE COURTS\nIn her conduct of the office of Attorney General of the United States, Pamela Bondi, contrary to her oath faithfully to execute the office of Attorney General of the United States and, to the best of her ability preserve, protect, and defend the Constitution of the United States, and in violation of her constitutional duty to take care that the laws be faithfully executed, has engaged in conduct that impaired the due and proper administration of justice, usurped the authority of the judiciary, and dismantles the rule of law that governs our country and protects the constitutional rights of its citizens and residents. She has, acting personally and through her subordinates and agents, intentionally and repeatedly defied court orders, acted purposefully to evade court oversight, and lied to or mislead judges and court administrators; and she has done so to enable Trump to carry out actions, policies, and practices that violate U.S. law, the U.S. Constitution, court orders, and the constitutional right of citizens and residents. The means used to implement this course of conduct or plan include, but is not limited to, one or more of the following, carried out personally or with through her subordinates and agents:\n**(1)**\nLying to or withholding information from the courts in making an error-filled presentation of the James Comey indictment to the grand jury disclose the existence of a memo from prosecutors against the prosecution of James Comey.\n**(2)**\nWithholding information about an applicable law from a magistrate judge to obtain a warrant to search and seize materials from a journalist\u2019s home.\n**(3)**\nMisleading a judge about the involvement of senior officials in the decision to bring criminal charges against Kilmar Abrego Garcia.\n**(4)**\nPresenting demonstrably false allegations in court to support baseless prosecutions against protesters; and inaccurately presenting the law to the court.\nThese acts individually and\n                together demonstrate that the Attorney General has defied and usurped the authority\n                afforded by our Constitution to the judiciary, and has a dangerous disregard for the\n                Constitution and the careful balance of powers that protects our country from abuses\n                by any single branch. In all of this, Pamela Bondi has acted in a manner contrary to\n                her trust as Attorney General and subversive of constitutional government, to the\n                great prejudice of the cause of law and justice and to the manifest injury of the\n                people of the United States. Wherefore Pamela Bondi, by such conduct, warrants\n                impeachment and trial, and removal from office.\n#### ARTICLE V: PERJURY IN CONGRESSIONAL TESTIMONY\nIn her conduct of the office of Attorney General of the United States, Pamela Bondi, contrary to her oath faithfully to execute the office of Attorney General of the United States and, to the best of her ability preserve, protect, and defend the Constitution of the United States, and in violation of her constitutional duty to take care that the laws be faithfully executed, has engaged in conduct that impaired the due and proper administration of justice, usurped the authority of the judiciary, and dismantles the rule of law that governs our country and protects the constitutional rights of its citizens and residents. She has lied to or misled Members of Congress after being sworn to tell the truth and she has done so to enable Trump to carry out actions, policies, and practices that violate U.S. law, the U.S. Constitution, court orders, and the constitutional rights of citizens and residents. The means used to implement this course of conduct or plan include, but are not limited to, one or more of the following, carried out personally:\n**(1)**\nOn January 15, 2025, Pamela Bondi swore to tell the truth, the whole truth, and nothing but the truth before the Senate Judiciary Committee for her nomination hearing. Contrary to that oath, Pamela Bondi willfully provided perjurious, false and misleading testimony to the Senate Judiciary Committee concerning one or more of the following: politicizing and weaponizing the DOJ and targeting journalists. Such testimony includes the following:\nSenator Whitehouse Question: Under what circumstances would you\n                        prosecute journalists for what they write?\nPamela Bondi Answer: I believe in the freedom of speech, only if\n                        anyone commits a crime.\nPamela Bondi Answer: .\u2002.\u2002.if I am Attorney General, I will not\n                        politicize that office, I will not target people simply because of their\n                        political affiliation. Justice will be administered even handedly throughout\n                        this country.\n**(2)**\nOn February 11, 2026, Pamela Bondi swore to tell the truth, the whole truth, and nothing but the truth before the House Judiciary Committee. Contrary to that oath, Pamela Bondi willfully provided perjurious, false and misleading testimony to the House Judiciary Committee concerning one or more of the following: the nature of Ghislaine Maxwell\u2019s detention in the Bureau of Prisons and the evidence against Donald J. Trump in the Epstein investigation. Such testimony includes the following:\nRepresentative Ross Question: Does a convicted sex offender like\n                        Ghislaine Maxwell deserve special treatment in prison and special privileges\n                        in prison?\nPamela Bondi Answer: I did not know she was being transferred, and\n                        she was not transferred to a lower-level facility.\nRepresentative Lieu Question: I want to know were there any underage\n                        girls at that party or at any party that Trump attended with Jeffrey\n                        Epstein?\nPamela Bondi Answer: .\u2002.\u2002.there is no evidence that Donald Trump has\n                        committed a crime.\nThese acts individually and\n                together demonstrate that the Attorney General has defied and usurped the authority\n                afforded by our Constitution to the judiciary, and has a dangerous disregard for the\n                Constitution and the careful balance of powers that protects our country from abuses\n                by any single branch. In all of this, Pamela Bondi has acted in a manner contrary to\n                her trust as Attorney General and subversive of constitutional government, to the\n                great prejudice of the cause of law and justice and to the manifest injury of the\n                people of the United States. Wherefore Pamela Bondi, by such conduct, warrants\n                impeachment and trial, and removal from office.",
      "versionDate": "2026-03-17",
      "versionType": "IH"
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
        "updateDate": "2026-03-19T15:34:57Z"
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
      "date": "2026-03-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1119ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Impeaching Pamela Bondi, Attorney General of the United States, for high crimes and misdemeanors.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-18T08:18:38Z"
    },
    {
      "title": "Impeaching Pamela Bondi, Attorney General of the United States, for high crimes and misdemeanors.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-18T08:06:32Z"
    }
  ]
}
```
